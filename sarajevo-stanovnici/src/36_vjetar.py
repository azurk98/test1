"""Vjetar za aerodrom: Butmir (METAR 2016–2025) i stanice FHMZ (SYNOP preko OGIMET-a, 2021–2025).

Stanice: Sarajevo-Bjelave 632 m, Ivan Sedlo 970 m (sedlo, visinom kao Nišići), Bjelašnica 2053 m
(slobodna atmosfera iznad planina). Bočni vjetar = brzina · |sin(smjer − smjer piste)|; tišina i
varijabilan vjetar se računaju kao 0. ICAO: pista treba biti upotrebljiva ≥ 95% vremena uz bočni
vjetar do 20 kt (za piste ≥ 1.500 m). Pista Butmira 119°/299°, a za Nišiće je predložena ~005°/185°.
Preuzimanje: raw/metar_lqsa_vjetar.csv (Iowa Environmental Mesonet) i raw/synop/<stanica>_<mjesec>.txt
(OGIMET getsynop, jedan mjesec po zahtjevu). Izlaz: out/vjetar_stanice.csv.
"""
from common import OUT, RAW
import pandas as pd, numpy as np, glob, re, sys
def synop(st):
    rows=[]
    for f in sorted(glob.glob(str(RAW / 'synop' / f'{st}_*.txt'))):
        for line in open(f):
            p=line.strip().split(',')
            if len(p)<7: continue
            g=p[6].replace('==','').split()
            try:
                i=g.index(str(st))
                yyggi=g[i-1]; iw=int(yyggi[4]); nddff=g[i+2]
                dd=nddff[1:3]; ff=nddff[3:5]
                if not (dd.isdigit() and ff.isdigit()): continue
                dd=int(dd)*10; ff=int(ff)
                if ff==99: ff=int(g[i+3][2:5])
                kt=ff*1.944 if iw in (0,1) else ff
                gust=np.nan
                # 333 911ff gust group
                if '333' in g:
                    for x in g[g.index('333')+1:]:
                        if x.startswith('910') or x.startswith('911'):
                            v=int(x[3:5]); gust=v*1.944 if iw in (0,1) else v; break
                if dd>360 and dd!=990: continue
                rows.append((pd.Timestamp(int(p[1]),int(p[2]),int(p[3]),int(p[4])), 0 if dd in (0,990) else dd, kt, gust, dd==990))
            except Exception: pass
    return pd.DataFrame(rows,columns=['t','dir','kt','gust','varijabilno']).drop_duplicates('t')
def metar():
    d=pd.read_csv(RAW / 'metar_lqsa_vjetar.csv',na_values='M',low_memory=False)
    d['t']=pd.to_datetime(d.valid); d=d.dropna(subset=['sknt']); d=d.set_index('t').resample('h').first().dropna(subset=['sknt']).reset_index()
    return pd.DataFrame({'t':d.t,'dir':d.drct.fillna(0),'kt':d.sknt,'gust':d.gust,'varijabilno':d.drct.isna()})
def ocjena(d, rwy):
    a=np.radians(d.dir-rwy); cw=np.abs(d.kt*np.sin(a)); cw[d.varijabilno|(d.kt<3)]=np.where(d.varijabilno|(d.kt<3), d.kt*0, cw)[d.varijabilno|(d.kt<3)]
    return cw
def opis(name,d,rwy):
    cw=ocjena(d,rwy); g=d.gust.fillna(d.kt)
    best=max(range(0,180,5), key=lambda r:(ocjena(d,r)<=13).mean())
    rose=d[d.kt>=3].assign(s=lambda x:((x.dir%360)//45*45).astype(int)).groupby('s').size()/ (d.kt>=3).sum()*100
    return {'stanica':name,'sati':len(d),'tiho_<3kt_%':round((d.kt<3).mean()*100),'srednja_kt':round(d.kt.mean(),1),
            'p95_kt':round(d.kt.quantile(.95)),'udari>=25kt_%':round((g>=25).mean()*100,2),'udari>=35kt_%':round((g>=35).mean()*100,2),
            f'bocni<=13kt_%_pista{rwy}':round((cw<=13).mean()*100,1),f'bocni<=20kt_%_pista{rwy}':round((cw<=20).mean()*100,2),
            'najbolji_smjer':best,'bocni<=13kt_%_najbolji':round((ocjena(d,best)<=13).mean()*100,1),
            'ruza_%':{int(k):round(v) for k,v in rose.items()}}
out=[opis('Butmir (METAR)',metar(),119)]
for st,n,rwy in ((14654,'Sarajevo-Bjelave 632 m',119),(14650,'Ivan Sedlo 970 m',5),(14652,'Bjelašnica 2053 m',5)):
    d=synop(st)
    if len(d): out.append(opis(n,d,rwy))
r = pd.DataFrame(out)
r.to_csv(OUT / 'vjetar_stanice.csv', index=False)
pd.set_option('display.width', 250)
print(r.drop(columns='ruza_%').to_string(index=False))
for o in out:
    print(o['stanica'], 'ruža (% sati, smjer od kojeg puše):', o['ruza_%'])
