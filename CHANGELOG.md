# Changelog

All notable changes to Power Flow are listed here.

## [1.1.0] – 2026-11-17

### Added

- Automatic accent themes **Power Flow Smaragd**, **Violett**, **Türkis** and **Koralle**. Like **Power Flow**, they follow the device's light/dark setting.
- README: what works without card-mod, and how to change the color of switched-on `pf_tile` tiles (`pf-active-rgb`).
- This changelog.

### Changed

- card-mod is now listed as recommended instead of required. Colors, card shape and light/dark mode work without it.
- `tools/gen_variants.py` also generates the automatic accent themes.

### Fixed

- README: HACS / the Marketplace installs the theme to `/config/themes/power_flow/power_flow.yaml`, not `/config/themes/power_flow.yaml`.

## [1.0.1] – 2026-11-13

### Changed

- HACS validation runs without exceptions, using the workflow from the official HACS example.

## [1.0.0] – 2026-11-13

First release.

- Themes **Power Flow Dark**, **Power Flow Light** and **Power Flow** (automatic).
- Accent variants Smaragd, Violett, Türkis and Koralle, each dark and light, with the same luminance as the original blue.
- card-mod styling for every dashboard card: hover glow, keyboard focus ring, fixed-width digits, reduced motion, fixes for power-flow-card-plus, price-timeline-card and solar-bar-card.
- button-card templates `pf_tile`, `pf_mini` and `pf_stat_card`.
- README in English and German, MIT license, preview images.

[1.1.0]: https://github.com/wattie2k1/power-flow-theme/releases/tag/v1.1.0
[1.0.1]: https://github.com/wattie2k1/power-flow-theme/releases/tag/v1.0.1
[1.0.0]: https://github.com/wattie2k1/power-flow-theme/releases/tag/v1.0.0
