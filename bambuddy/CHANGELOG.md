<!-- https://developers.home-assistant.io/docs/add-ons/presentation#keeping-a-changelog -->

# Changelog

All notable changes to the App will be documented in this file.
## [0.2.4.1-4] - 2026-05-17

- **Build**: Migrated deprecated `build.yaml` options to Dockerfile `ARG` directives.
- **Fix**: Replaced broken `py3-opencv` + `sed` workaround with HA's precompiled musllinux wheels for `opencv-python-headless`, fixing empty plate detection.
- **Fix**: Corrected `HA_URL` supervisor path to `http://supervisor/core` (Bambuddy appends its own `/api/` path).

## [0.2.4.1-3] - 2026-05-16

- **Auto-Discovery**: Fixed an issue where the MQTT broker auto-discovery successfully fetched credentials but failed to automatically toggle `MQTT_ENABLED=true`.

## [0.2.4.1-2] - 2026-05-16

- **Fix**: Corrected the file path in the Dockerfile notification patch to properly apply during build.

## [0.2.4.1-1] - 2026-05-16

- **Fix**: Injected a dynamic patch into the Bambuddy backend to automatically map legacy notification schemas to the new Home Assistant 2024.6+ `notify.send_message` entity architecture.
- **Dependency**: Pulled downstream Renovate bot updates for OrcaSlicer and BambuStudio container dependencies.

## [0.2.4.1-0] - 2026-05-16

- **Upstream Bump**: Updated base Bambuddy image to `0.2.4.1`

## [0.2.4-1] - 2026-05-16

- **Fix**: Reverted Home Assistant API URL to properly route notification service calls.
- **Auto-Discovery**: Added `bashio::services` integration to auto-discover MQTT broker credentials from Home Assistant if left as defaults in the UI config.

## [0.2.4] - 2026-05-15

- **Networking**: Switched to `host_network: true` to support SSDP discovery and Virtual Printer FTP file transfers.
- **Proxy**: Removed internal NGINX proxy to resolve `8099` port conflicts with Zigbee2MQTT.
- **Home Assistant API**: Seamlessly injected via Supervisor token (no manual UI setup required).
- **MQTT**: Added complete configurable integration with local Mosquitto brokers.
