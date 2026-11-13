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
themes/power_flow.yaml               Theme-Datei (alle Themes), wird von HACS installiert
hacs.json                            HACS-Beschreibung des Repos
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

In `configuration.yaml` müssen Themes aus dem Ordner `themes` geladen werden:

```yaml
frontend:
  themes: !include_dir_merge_named themes
```

### Über HACS / Marketplace

1. HACS (bzw. ab HA 2026.11 **Einstellungen → Marketplace**) öffnen.
2. Menü ⋮ → **Benutzerdefinierte Repositories** (Marketplace: **Aus Link hinzufügen**), URL dieses Repos eintragen, Kategorie **Theme**.
3. „Power Flow“ suchen und herunterladen. Die Datei landet unter `/config/themes/power_flow.yaml`.
4. Aktion `frontend.reload_themes` ausführen und im Profil das Theme wählen.

Updates erscheinen danach automatisch in HACS / im Marketplace.

### Manuell

`themes/power_flow.yaml` nach `/config/themes/` kopieren, dann `frontend.reload_themes` ausführen.

> Nicht beide Wege gleichzeitig nutzen: Liegt die Datei doppelt unter `/config/themes/`, sind die Themes doppelt definiert.

### button-card-Templates

Die Templates installiert HACS nicht mit. Sie gehören in die Dashboard-Konfiguration unter `button_card_templates:` (Dashboard → Rohkonfiguration bearbeiten).

## Varianten neu erzeugen

`tools/gen_variants.py` berechnet die Akzentfarben und Primär-Skalen und schreibt `variants.yaml`. Den Block ersetzt man in der Theme-Datei ab „AKZENT-VARIANTEN“.
