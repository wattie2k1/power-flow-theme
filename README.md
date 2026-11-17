# Power Flow – Home Assistant Theme

**English** · [Deutsch](#deutsch)

A custom Home Assistant theme (tested with HA OS, Core 2026.11). With card-mod installed, it also adds extra styling to every dashboard card.

![Power Flow Dark – example tiles](images/preview-dark.png)

![Power Flow Light – example tiles](images/preview-light.png)

## Included themes

| Theme | Mode | Accent |
|---|---|---|
| Power Flow Dark | dark | blue |
| Power Flow Light | light | blue |
| Power Flow | automatic (follows the device) | blue |
| Power Flow Dark/Light Smaragd | dark / light | emerald green |
| Power Flow Dark/Light Violett | dark / light | violet |
| Power Flow Dark/Light Türkis | dark / light | turquoise |
| Power Flow Dark/Light Koralle | dark / light | coral red |
| Power Flow Smaragd / Violett / Türkis / Koralle | automatic (follows the device) | as above |

All accent variants have the same luminance as the original blue, so the WCAG contrast ratios stay the same.

## Repository layout

```
themes/power_flow.yaml               theme file (all themes), installed by HACS
hacs.json                            HACS metadata
button-card-templates/               button-card templates used in the dashboards
  haussteuerung.yaml                 pf_tile (switch tile), pf_mini (small action buttons)
  energie-uebersicht.yaml            pf_stat_card (statistics card)
tools/gen_variants.py                generates the accent variants
tools/make_preview.py                generates the preview images (SVG, in images/)
images/                              preview images for the README and HACS
```

Shared parts exist only once in the theme file, as YAML anchors:

- `&pf_card_mod`: CSS applied to every dashboard card (hover, focus, rules per card type)
- `&pf_map`: maps all HA variables to the `pf-*` palette
- `&pf_dark_mode` / `&pf_light_mode`: the two palettes

The variants take over a palette with `<<:` and only override the accent colors.

## Installation

Requirements: none. The colors, backgrounds, card shape (radius, border, shadow), light/dark mode and all accent variants use standard Home Assistant theme variables.

Recommended: [card-mod](https://github.com/thomasloven/lovelace-card-mod). Without it, these extras are missing:

- accent border and glow when hovering a card with the mouse
- visible focus ring for keyboard navigation
- fixed-width digits, so changing values do not jump
- no animations when the device is set to “reduce motion”
- matching colors and backgrounds for power-flow-card-plus, price-timeline-card and solar-bar-card
- the `pf-stat` and `pf-mini` card classes

Optional: [button-card](https://github.com/custom-cards/button-card) for the templates in `button-card-templates/`. `pf_tile` works without card-mod.

`configuration.yaml` must load themes from the `themes` folder:

```yaml
frontend:
  themes: !include_dir_merge_named themes
```

### Via HACS / Marketplace

1. Open HACS (or, from HA 2026.11, **Settings → Marketplace**).
2. Menu ⋮ → **Custom repositories** (Marketplace: **Add from link**), enter this repository's URL, category **Theme**.
3. Search for “Power Flow” and download it. The file is placed at `/config/themes/power_flow/power_flow.yaml`.
4. Run the action `frontend.reload_themes` and pick the theme in your profile.

Updates then show up automatically in HACS / the Marketplace.

### Manual

Copy `themes/power_flow.yaml` to `/config/themes/`, then run `frontend.reload_themes`.

> Do not use both ways at once: if the file exists twice under `/config/themes/` (e.g. `power_flow.yaml` and `power_flow/power_flow.yaml`), every theme is defined twice. If you already copied it to `/config/themes/power_flow/power_flow.yaml` by hand, HACS / the Marketplace will overwrite that file.

### button-card templates

HACS does not install the templates. Add them to the dashboard configuration under `button_card_templates:` (dashboard → edit raw configuration).

Switched-on `pf_tile` tiles use the theme variable `pf-active-rgb` (orange by default: `255, 152, 0` dark, `207, 117, 0` light). To use a different color, change it in both palettes of the theme file. Note that an update via HACS / the Marketplace replaces the file.

## Regenerating the variants

`tools/gen_variants.py` calculates the accent colors and primary scales and writes `variants.yaml`. Replace the block in the theme file starting at “AKZENT-VARIANTEN” with it.

## License

Changes: see [CHANGELOG](CHANGELOG.md).

MIT, see [LICENSE](LICENSE).

---

<a id="deutsch"></a>

# Power Flow – Home-Assistant-Theme

[English](#power-flow--home-assistant-theme) · **Deutsch**

Eigenes Theme für Home Assistant (getestet mit HA OS, Core 2026.11). Mit card-mod gestaltet es zusätzlich jede Dashboard-Karte. Vorschaubilder siehe oben.

## Enthaltene Themes

| Theme | Modus | Akzent |
|---|---|---|
| Power Flow Dark | dunkel | Blau |
| Power Flow Light | hell | Blau |
| Power Flow | automatisch (folgt dem Gerät) | Blau |
| Power Flow Dark/Light Smaragd | dunkel / hell | Grün |
| Power Flow Dark/Light Violett | dunkel / hell | Violett |
| Power Flow Dark/Light Türkis | dunkel / hell | Türkis |
| Power Flow Dark/Light Koralle | dunkel / hell | Korallrot |
| Power Flow Smaragd / Violett / Türkis / Koralle | automatisch (folgt dem Gerät) | wie oben |

Alle Akzent-Varianten haben dieselbe Leuchtdichte wie das Original-Blau, die WCAG-Kontraste bleiben also gleich.

## Aufbau

```
themes/power_flow.yaml               Theme-Datei (alle Themes), wird von HACS installiert
hacs.json                            HACS-Beschreibung des Repos
button-card-templates/               button-card-Templates der Dashboards
  haussteuerung.yaml                 pf_tile (Schalter-Kachel), pf_mini (kleine Aktionsbuttons)
  energie-uebersicht.yaml            pf_stat_card (Kennzahl-Karte)
tools/gen_variants.py                erzeugt die Akzent-Varianten
tools/make_preview.py                erzeugt die Vorschaubilder (SVG, in images/)
images/                              Vorschaubilder für README und HACS
```

In der Theme-Datei gibt es die gemeinsamen Teile nur einmal, als YAML-Anker:

- `&pf_card_mod`: CSS für jede Dashboard-Karte (Hover, Fokus, Kartentyp-Regeln)
- `&pf_map`: Zuordnung aller HA-Variablen zur `pf-*`-Palette
- `&pf_dark_mode` / `&pf_light_mode`: die beiden Paletten

Die Varianten übernehmen eine Palette per `<<:` und überschreiben nur die Akzentfarben.

## Installation

Voraussetzungen: keine. Farben, Hintergründe, Kartenform (Rundung, Rahmen, Schatten), Hell/Dunkel und alle Akzent-Varianten laufen über normale Home-Assistant-Theme-Variablen.

Empfohlen: [card-mod](https://github.com/thomasloven/lovelace-card-mod). Ohne card-mod fehlen:

- Akzent-Rahmen und Schein beim Überfahren einer Karte mit der Maus
- sichtbarer Fokusrahmen bei Bedienung mit der Tastatur
- gleich breite Ziffern, damit wechselnde Werte nicht springen
- keine Animationen, wenn am Gerät „Bewegung reduzieren“ eingestellt ist
- passende Farben und Hintergründe für power-flow-card-plus, price-timeline-card und solar-bar-card
- die Kartenklassen `pf-stat` und `pf-mini`

Optional: [button-card](https://github.com/custom-cards/button-card) für die Templates in `button-card-templates/`. `pf_tile` funktioniert ohne card-mod.

In `configuration.yaml` müssen Themes aus dem Ordner `themes` geladen werden:

```yaml
frontend:
  themes: !include_dir_merge_named themes
```

### Über HACS / Marketplace

1. HACS (bzw. ab HA 2026.11 **Einstellungen → Marketplace**) öffnen.
2. Menü ⋮ → **Benutzerdefinierte Repositories** (Marketplace: **Aus Link hinzufügen**), URL dieses Repos eintragen, Kategorie **Theme**.
3. „Power Flow“ suchen und herunterladen. Die Datei landet unter `/config/themes/power_flow/power_flow.yaml`.
4. Aktion `frontend.reload_themes` ausführen und im Profil das Theme wählen.

Updates erscheinen danach automatisch in HACS / im Marketplace.

### Manuell

`themes/power_flow.yaml` nach `/config/themes/` kopieren, dann `frontend.reload_themes` ausführen.

> Nicht beide Wege gleichzeitig nutzen: Liegt die Datei doppelt unter `/config/themes/` (z. B. `power_flow.yaml` und `power_flow/power_flow.yaml`), sind die Themes doppelt definiert. Liegt sie schon von Hand unter `/config/themes/power_flow/power_flow.yaml`, überschreibt HACS bzw. der Marketplace diese Datei.

### button-card-Templates

Die Templates installiert HACS nicht mit. Sie gehören in die Dashboard-Konfiguration unter `button_card_templates:` (Dashboard → Rohkonfiguration bearbeiten).

Eingeschaltete `pf_tile`-Kacheln nutzen die Theme-Variable `pf-active-rgb` (Standard Orange: `255, 152, 0` dunkel, `207, 117, 0` hell). Für eine andere Farbe den Wert in beiden Paletten der Theme-Datei ändern. Achtung: Ein Update über HACS bzw. den Marketplace ersetzt die Datei.

## Varianten neu erzeugen

`tools/gen_variants.py` berechnet die Akzentfarben und Primär-Skalen und schreibt `variants.yaml`. Den Block ersetzt man in der Theme-Datei ab „AKZENT-VARIANTEN“.

## Lizenz

Änderungen: siehe [CHANGELOG](CHANGELOG.md).

MIT, siehe [LICENSE](LICENSE).
