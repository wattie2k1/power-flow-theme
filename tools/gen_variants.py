import colorsys, sys
def h2rgb(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16)/255 for i in (0,2,4))
def rgb2h(c): return '#'+''.join(f'{round(max(0,min(1,x))*255):02x}' for x in c)
def lin(x): return x/12.92 if x<=0.04045 else ((x+0.055)/1.055)**2.4
def lum(c): r,g,b=[lin(x) for x in c]; return 0.2126*r+0.7152*g+0.0722*b
def contrast(a,b):
    la,lb=sorted([lum(h2rgb(a)),lum(h2rgb(b))],reverse=True); return (la+.05)/(lb+.05)
def match(ref, hue, sat_scale=1.0):
    """Farbe mit Farbton hue, Sättigung wie ref, gleicher Leuchtdichte wie ref."""
    rr=h2rgb(ref); _,_,s=colorsys.rgb_to_hls(*rr); s=min(1,s*sat_scale); target=lum(rr)
    lo,hi=0.0,1.0
    for _ in range(40):
        m=(lo+hi)/2; c=colorsys.hls_to_rgb(hue/360,m,s)
        if lum(c)<target: lo=m
        else: hi=m
    return rgb2h(colorsys.hls_to_rgb(hue/360,(lo+hi)/2,s))
def rgbtxt(h): return ', '.join(str(round(x*255)) for x in h2rgb(h))
SCALE={'05':'#04172f','10':'#082447','20':'#0e3b72','30':'#16529e','40':'#1f6dcd','50':'#3b92f4',
       '60':'#64aaf7','70':'#8fc2fa','80':'#b9d9fc','90':'#dceafd','95':'#eef5fe'}
DARK={'pf-accent':'#3b92f4','pf-accent-container':'#23364c'}
LIGHT={'pf-accent':'#1f6dcd','pf-accent-container':'#dce9fb','pf-on-accent-container':'#0f3a73'}
VARIANTS=[('Smaragd',150,0.85),('Violett',262,1.0),('Türkis',178,0.9),('Koralle',352,0.95)]
out=[]
out.append('''
# =================================================================
# AKZENT-VARIANTEN (2026-11-09)
# Jede Variante übernimmt die komplette Dark- bzw. Light-Palette per
# Merge und überschreibt NUR die Akzentfarben + die Primär-Skala.
# Die Werte haben dieselbe Leuchtdichte wie das Original-Blau, damit
# alle Kontraste (WCAG) identisch bleiben. Erzeugt mit gen_variants.py.
# =================================================================''')
report=[]
for name,hue,ss in VARIANTS:
    scale={k:match(v,hue,ss) for k,v in SCALE.items()}
    for mode,base,anchor in (('dark',DARK,'pf_dark_mode'),('light',LIGHT,'pf_light_mode')):
        vals={k:match(v,hue,ss) for k,v in base.items()}
        if mode=='dark': vals['pf-on-accent-container']='#ffffff'
        title=f'Power Flow {"Dark" if mode=="dark" else "Light"} {name}'
        out.append(f'\n"{title}":\n  card-mod-theme: "{title}"\n  card-mod-card: *pf_card_mod\n  modes:\n    {mode}:\n      <<: *{anchor}')
        for k,v in vals.items(): out.append(f"      {k}: '{v}'")
        out.append(f"      rgb-primary-color: '{rgbtxt(vals['pf-accent'])}'")
        for k,v in scale.items(): out.append(f"      ha-color-primary-{k}: '{v}'")
        surf='#182430' if mode=='dark' else '#ffffff'
        report.append(f"{title:30} accent {vals['pf-accent']}  vs Karte {contrast(vals['pf-accent'],surf):.2f}  weiß {contrast(vals['pf-accent'],'#ffffff'):.2f}  container {vals['pf-accent-container']}")
open('variants.yaml','w').write('\n'.join(out)+'\n')
print('\n'.join(report))
print('Original Dark  vs Karte %.2f weiß %.2f'%(contrast('#3b92f4','#182430'),contrast('#3b92f4','#ffffff')))
print('Original Light vs Karte %.2f'%contrast('#1f6dcd','#ffffff'))
