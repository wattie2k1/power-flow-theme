# Power Flow – Home-Assistant-Theme

Eigenes Theme für Home Assistant (getestet mit HA OS, Core 2026.11) mit card-mod-Styling für alle Dashboard-Karten.

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

Alle Akzent-Varianten haben dieselbe Leuchtdichte wie das Original-Blau, die WCAG-Kontraste bleiben also gleich.

## Aufbau

```
themes/power_flow/power_flow.yaml   Theme-Datei (alle Themes)
button-card-templates/               button-card-Templates der Dashboards
  haussteuerung.yaml                 pf_tile (Schalter-Kachel), pf_mini (kleine Aktionsbuttons)
  energie-uebersicht.yaml            pf_stat_card (Kennzahl-Karte)
tools/gen_variants.py                erzeugt die Akzent-Varianten
```

In der Theme-Datei gibt es die gemeinsamen Teile nur einmal, als YAML-Anker:

- `&pf_card_mod`: CSS für jede Dashboard-Karte (Hover, Fokus, Kartentyp-Regeln)
- `&pf_map`: Zuordnung aller HA-Variablen zur `pf-*`-Palette
- `&pf_dark_mode` / `&pf_light_mode`: die beiden Paletten

Die Varianten übernehmen eine Palette per `<<:` und überschreiben nur die Akzentfarben.

## Installation

Voraussetzungen: [card-mod](https://github.com/thomasloven/lovelace-card-mod) und für die Templates [button-card](https://github.com/custom-cards/button-card).

1. `themes/power_flow/` nach `/config/themes/` kopieren.
2. In `configuration.yaml`:
   ```yaml
   frontend:
     themes: !include_dir_merge_named themes
   ```
3. Aktion `frontend.reload_themes` ausführen und im Profil das Theme wählen.

Die button-card-Templates gehören in die Dashboard-Konfiguration unter `button_card_templates:` (Dashboard → Rohkonfiguration bearbeiten).

## Varianten neu erzeugen

`tools/gen_variants.py` berechnet die Akzentfarben und Primär-Skalen und schreibt `variants.yaml`. Den Block ersetzt man in der Theme-Datei ab „AKZENT-VARIANTEN“.
