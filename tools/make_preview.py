"""Erzeugt die Vorschaubilder images/preview-dark.svg und images/preview-light.svg
mit Beispielkacheln im Stil des pf_tile-Templates (Farben aus der Theme-Palette)."""
import os
PLUG = "M16,7V3H14V7H10V3H8V7H8C7,7 6,8 6,9V14.5L9.5,18V21H14.5V18L18,14.5V9C18,8 17,7 16,7Z"
BULB = "M12,2A7,7 0 0,0 5,9C5,11.38 6.19,13.47 8,14.74V17A1,1 0 0,0 9,18H15A1,1 0 0,0 16,17V14.74C17.81,13.47 19,11.38 19,9A7,7 0 0,0 12,2M9,21A1,1 0 0,0 10,22H14A1,1 0 0,0 15,21V20H9V21Z"
TV = "M21,17H3V5H21M21,3H3A2,2 0 0,0 1,5V17A2,2 0 0,0 3,19H8V21H16V19H21A2,2 0 0,0 23,17V5A2,2 0 0,0 21,3Z"
FAN = "M12,11A1,1 0 0,0 11,12A1,1 0 0,0 12,13A1,1 0 0,0 13,12A1,1 0 0,0 12,11M12.5,2C17,2 17.11,5.57 14.75,6.75C13.76,7.24 13.32,8.29 13.13,9.22C13.61,9.42 14.03,9.73 14.35,10.13C18.05,8.13 22.03,8.92 22.03,12.5C22.03,17 18.46,17.1 17.28,14.73C16.78,13.74 15.72,13.3 14.79,13.11C14.59,13.59 14.28,14 13.88,14.34C15.87,18.03 15.08,22 11.5,22C7,22 6.91,18.42 9.27,17.24C10.25,16.75 10.69,15.71 10.89,14.79C10.4,14.59 9.97,14.27 9.65,13.87C5.96,15.85 2,15.07 2,11.5C2,7 5.56,6.89 6.74,9.26C7.24,10.25 8.29,10.68 9.22,10.87C9.41,10.39 9.73,9.97 10.14,9.65C8.15,5.96 8.94,2 12.5,2Z"
THEMES = {
 "dark": dict(bg="#0b1016", card="#182430", border="#2d3f52", text="#ffffff", muted="#8d9fae", sec="#a0aec0",
              act="255,152,0", ov="255,255,255", title="Power Flow Dark", shadow="0,0,0", shop=0.45),
 "light": dict(bg="#eef2f7", card="#ffffff", border="#d5dde7", text="#0f1720", muted="#627080", sec="#4a5a6b",
               act="207,117,0", ov="15,23,32", title="Power Flow Light", shadow="15,23,32", shop=0.10),
}
TILES = [("Stehlampe", "vor 12 Minuten", BULB, True), ("Fernseher", "vor 2 Stunden", TV, False),
         ("Kaffeemaschine", "vor 3 Minuten", PLUG, True), ("Ventilator", "vor 1 Tag", FAN, False)]
W, H, TW, TH, GAP, PAD = 720, 330, 324, 96, 12, 24
FONT = "font-family=\"-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif\""
def tile(x, y, name, sub, icon, on, c):
    a, o = c["act"], c["ov"]
    out = []
    if on:
        out.append(f'<rect x="{x}" y="{y}" width="{TW}" height="{TH}" rx="16" fill="rgba({a},0.16)" filter="url(#glow)"/>')
    out.append(f'<rect x="{x}" y="{y}" width="{TW}" height="{TH}" rx="16" fill="{c["card"]}" filter="url(#sh)"/>')
    if on:
        out.append(f'<rect x="{x}" y="{y}" width="{TW}" height="{TH}" rx="16" fill="url(#on)"/>')
    stroke = f"rgba({a},0.55)" if on else c["border"]
    out.append(f'<rect x="{x+.5}" y="{y+.5}" width="{TW-1}" height="{TH-1}" rx="15.5" fill="none" stroke="{stroke}"/>')
    ix, iy = x + 16, y + (TH - 46) / 2
    out.append(f'<rect x="{ix+.5}" y="{iy+.5}" width="45" height="45" rx="11.5" fill="rgba({a if on else o},{0.16 if on else 0.09})" '
               f'stroke="rgba({a if on else o},{0.35 if on else 0.20})"/>')
    col = f"rgb({a})" if on else c["sec"]
    out.append(f'<path d="{icon}" fill="{col}" transform="translate({ix+11},{iy+11})"/>')
    if not on and icon == PLUG:
        out.append(f'<line x1="{ix+12}" y1="{iy+12}" x2="{ix+34}" y2="{iy+34}" stroke="{col}" stroke-width="2"/>')
    tx = ix + 46 + 12
    out.append(f'<text x="{tx}" y="{y+44}" {FONT} font-size="15" font-weight="700" fill="{c["text"]}">{name}</text>')
    out.append(f'<text x="{tx}" y="{y+64}" {FONT} font-size="12" fill="{c["muted"]}">{sub}</text>')
    return "\n".join(out)
for mode, c in THEMES.items():
    a = c["act"]
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
         '<defs>',
         f'<linearGradient id="on" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="rgb({a})" stop-opacity="0.18"/>'
         f'<stop offset="0.55" stop-color="rgb({a})" stop-opacity="0.05"/><stop offset="1" stop-color="rgb({a})" stop-opacity="0.02"/></linearGradient>',
         '<filter id="glow" x="-20%" y="-30%" width="140%" height="170%"><feGaussianBlur stdDeviation="9"/></filter>',
         f'<filter id="sh" x="-10%" y="-10%" width="120%" height="140%"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="rgb({c["shadow"]})" flood-opacity="{c["shop"]}"/></filter>',
         '</defs>',
         f'<rect width="{W}" height="{H}" rx="20" fill="{c["bg"]}"/>',
         f'<text x="{PAD}" y="{PAD+18}" {FONT} font-size="17" font-weight="600" fill="{c["text"]}">Wohnzimmer</text>',
         f'<text x="{W-PAD}" y="{PAD+18}" {FONT} font-size="12" text-anchor="end" fill="{c["muted"]}">{c["title"]}</text>']
    for i, t in enumerate(TILES):
        x = PAD + (i % 2) * (TW + GAP)
        y = PAD + 40 + (i // 2) * (TH + GAP)
        s.append(tile(x, y, *t, c))
    s.append(f'<text x="{PAD}" y="{H-PAD+4}" {FONT} font-size="11" fill="{c["muted"]}">Beispielkacheln mit dem button-card-Template pf_tile</text>')
    s.append('</svg>')
    path = os.path.join(os.path.dirname(__file__), "..", "images", f"preview-{mode}.svg")
    open(path, "w").write("\n".join(s))
    print("geschrieben:", os.path.normpath(path))
