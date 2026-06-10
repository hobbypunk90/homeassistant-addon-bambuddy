# Bambuddy Obico ML API

A self-hosted, headless Obico ML API sidecar for [Bambuddy](https://github.com/connormxy/homeassistant-addon-bambuddy). This add-on provides AI-based print failure detection (spaghetti, layer shifts) without relying on cloud services.

This is a customized version of the Obico ML API that natively returns images with bounding boxes drawn over detected failures, allowing Bambuddy to send rich notifications with visual context directly to Home Assistant.

## Credits & Acknowledgements
This add-on is heavily based on and directly adapted from **[nobodyguy's obico_ml_ha_addon](https://github.com/nobodyguy/obico_ml_ha_addon)**. Huge thanks to them for pioneering the integration of the Obico ML API into the Home Assistant ecosystem.

The core AI engine is powered by the open-source **[Obico Server](https://github.com/TheSpaghettiDetective/obico-server)** project (formerly The Spaghetti Detective).

## Features
- Full local AI failure detection based on official Obico ML 1.4 models.
- Enhanced `/detect/` endpoint for returning pre-annotated bounding box snapshots (can be toggled off via config).
- Seamless integration with the Bambuddy add-on.

## Installation
This add-on is part of the Bambuddy Home Assistant add-on repository. Install it alongside the main Bambuddy add-on to enable local AI detection.

## Configuration
See [DOCS.md](DOCS.md) for configuration options.
