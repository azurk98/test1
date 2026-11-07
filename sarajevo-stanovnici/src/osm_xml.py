"""OSM XML ekstrakt (npr. BBBike Sarajewo.osm.gz) -> Overpass JSON (`out geom tags`).

Rezervni put kad Overpass nije dostupan: proizvodi raw/granice.json i
raw/osm_grad.json u istom obliku kao 01_preuzimanje.py, pa ostali koraci
ne vide razliku.
"""
from __future__ import annotations

import gzip
import json
import xml.etree.ElementTree as ET
from pathlib import Path


def _je_objekat(tags: dict, el_type: str) -> bool:
    if el_type == "node":
        return (any(k in tags for k in ("shop", "amenity", "office"))
                or ("addr:housenumber" in tags and "addr:street" in tags))
    return ("building" in tags or "landuse" in tags or tags.get("leisure") == "park"
            or tags.get("aeroway") == "aerodrome")


def konvertuj(xml_gz: Path, relacije: set[int], granice_out: Path, objekti_out: Path) -> dict:
    nodes: dict[int, tuple[float, float]] = {}
    ways: dict[int, list[int]] = {}
    way_tags: dict[int, dict] = {}
    rels: list[tuple[int, dict, list]] = []
    node_obj: list[dict] = []

    opener = gzip.open if str(xml_gz).endswith(".gz") else open
    with opener(xml_gz, "rb") as f:
        for _, el in ET.iterparse(f, events=("end",)):
            t = el.tag
            if t == "node":
                i = int(el.get("id"))
                lat, lon = float(el.get("lat")), float(el.get("lon"))
                nodes[i] = (lat, lon)
                tags = {c.get("k"): c.get("v") for c in el.findall("tag")}
                if tags and _je_objekat(tags, "node"):
                    node_obj.append({"type": "node", "id": i, "lat": lat, "lon": lon, "tags": tags})
                el.clear()
            elif t == "way":
                i = int(el.get("id"))
                ways[i] = [int(n.get("ref")) for n in el.findall("nd")]
                tags = {c.get("k"): c.get("v") for c in el.findall("tag")}
                if tags:
                    way_tags[i] = tags
                el.clear()
            elif t == "relation":
                i = int(el.get("id"))
                tags = {c.get("k"): c.get("v") for c in el.findall("tag")}
                mem = [(m.get("type"), int(m.get("ref")), m.get("role") or "") for m in el.findall("member")]
                if i in relacije or _je_objekat(tags, "relation"):
                    rels.append((i, tags, mem))
                el.clear()

    def geom(way_id: int):
        return [{"lat": nodes[n][0], "lon": nodes[n][1]} for n in ways.get(way_id, []) if n in nodes]

    def rel_el(i, tags, mem):
        members = [{"type": "way", "ref": r, "role": role, "geometry": geom(r)}
                   for typ, r, role in mem if typ == "way" and r in ways]
        return {"type": "relation", "id": i, "tags": tags, "members": members}

    granice, objekti = [], list(node_obj)
    nepotpune = []
    for i, tags, mem in rels:
        e = rel_el(i, tags, mem)
        if i in relacije:
            n_way = sum(1 for typ, *_ in mem if typ == "way")
            if len(e["members"]) < n_way:
                nepotpune.append(i)
            granice.append(e)
        if _je_objekat(tags, "relation"):
            objekti.append(e)
    for i, tags in way_tags.items():
        if _je_objekat(tags, "way"):
            objekti.append({"type": "way", "id": i, "tags": tags, "geometry": geom(i)})

    granice_out.write_text(json.dumps({"elements": granice}), encoding="utf-8")
    objekti_out.write_text(json.dumps({"elements": objekti}), encoding="utf-8")
    return {"granice": len(granice), "nedostaju_relacije": sorted(relacije - {e["id"] for e in granice}),
            "nepotpune_relacije": nepotpune, "objekti": len(objekti)}


def dopuni_relacije_iz_api(ids: list[int], granice_path: Path, ua: dict) -> list[int]:
    """Zamijeni nepotpune relacije punim verzijama s api.openstreetmap.org
    (/relation/{id}/full). Vraća ID-jeve koje nije uspjelo dopuniti."""
    import requests

    data = json.loads(granice_path.read_text(encoding="utf-8"))
    po_id = {e["id"]: e for e in data["elements"]}
    neuspjele = []
    for rid in ids:
        r = requests.get(f"https://api.openstreetmap.org/api/0.6/relation/{rid}/full",
                         headers=ua, timeout=120)
        if r.status_code != 200:
            neuspjele.append(rid)
            continue
        root = ET.fromstring(r.content)
        nodes = {int(n.get("id")): (float(n.get("lat")), float(n.get("lon"))) for n in root.iter("node")}
        ways = {int(w.get("id")): [int(n.get("ref")) for n in w.findall("nd")] for w in root.iter("way")}
        rel = next(x for x in root.iter("relation") if int(x.get("id")) == rid)
        tags = {c.get("k"): c.get("v") for c in rel.findall("tag")}
        members = []
        for m in rel.findall("member"):
            if m.get("type") != "way":
                continue
            ref = int(m.get("ref"))
            members.append({"type": "way", "ref": ref, "role": m.get("role") or "",
                            "geometry": [{"lat": nodes[n][0], "lon": nodes[n][1]}
                                         for n in ways.get(ref, []) if n in nodes]})
        po_id[rid] = {"type": "relation", "id": rid, "tags": tags, "members": members}
    data["elements"] = list(po_id.values())
    granice_path.write_text(json.dumps(data), encoding="utf-8")
    return neuspjele
