<!-- https://developers.home-assistant.io/docs/add-ons/presentation#keeping-a-changelog -->

# Changelog

All notable changes to the App will be documented in this file.

## [0.2.4.1-0.2.2] - 2026-05-19
- **First Stable Release**
- **Fix**: Resolved an encoding bug in the patch files that caused the Docker build process to fail on Home Assistant.

## [0.2.4.1-0.2] - 2026-05-19

*(Note: Version number has been rolled over from `-9.1` in preparation for an impending restructuring of the development workflow.)*

### Obico ML AI Integration
- **Bounding Boxes in Notifications**: Enhanced the Obico detection patches to request and pass along pre-drawn bounding boxes directly from the ML API, providing rich visual context in Home Assistant notifications when print failures occur.
- **MQTT Auto-Discovery**: Implemented fully native Home Assistant Auto-Discovery for the Obico ML integration. Bambuddy now automatically pushes and registers `obico_monitoring`, `obico_active`, and `obico_failed` as binary sensors directly tied to the printer device.
- **State Persistence (Anti-Strobe)**: Added intelligent `_failure_latched` state tracking. If a failure is detected, the failure and monitoring states persist through a print pause (even when the camera is not actively polling) to prevent chamber lights/automations from toggling off abruptly.

### Configuration & Sanitization
- **URL Auto-Correction**: Added runtime sanitization for `obico_ml_url`, `orcaslicer_api_url`, and `bambu_studio_api_url` to automatically prepend `http://` if a protocol was omitted.
- **MQTT Broker Validation**: Added regex sanitization to the `mqtt_broker` config to strip out invalid protocols (e.g., `mqtt://`, `http://`) and trailing ports passed by the user, ensuring clean connection handoffs.
- **UI Hints**: Updated `translations/en.yaml` to explicitly define how to format the URL and MQTT broker config inputs.

## [0.2.4.1-9.1] - 2026-05-18

### Documentation & UI
- **Config hint text**: Added `translations/en.yaml` — all add-on configuration fields now display human-readable names and concise descriptions in the Home Assistant UI.
- **Port conflict docs**: Expanded port conflict notes in `DOCS.md` for Z-Wave JS, Mosquitto TLS, and FTPS passive data ports.
- **German translation**: Removed placeholder German translation file; pending any localization updates.

## [0.2.4.1-9] - 2026-05-17

### Build & Install Optimizations
- **Base image**: Downgraded from Python 3.14 to **Python 3.11** (`3.11-alpine3.21`) to match the HA wheels server's precompiled `cp311` `opencv-python-headless` wheels — installs in ~5 minutes instead of failing on a 30+ minute source compilation.
- **Pip flags**: Added `--find-links` (HA musllinux wheel server), `--prefer-binary`, and a `numpy<2` constraint to guarantee prebuilt wheels and ABI compatibility.
- **BuildKit migration**: Moved deprecated `build.yaml` options into Dockerfile `ARG` directives.

### MQTT & Configuration
- **Zero-config MQTT**: MQTT fields are now blank by default in the add-on config. If the Mosquitto add-on is installed, credentials are auto-discovered from the supervisor — MQTT just works with no manual setup. User-configured values in either the add-on config or the Bambuddy web UI are respected and never silently overwritten.
- **Auto-discovery fix**: Fixed an issue where MQTT auto-discovery fetched credentials but failed to set `MQTT_ENABLED=true`.

### Fixes
- **HA notifications**: Injected a runtime patch for the Home Assistant 2024.6+ `notify.send_message` entity architecture.
- **Supervisor path**: Corrected `HA_URL` to `http://supervisor/core` (Bambuddy appends `/api/` internally).
- **Run script**: Fixed `rm -r` → `rm -rf` for idempotent data directory setup; removed template boilerplate.

### Internal
- **init_settings.py**: Renamed logger, simplified boolean handling, added documentation comments.

## [0.2.4.1-0] - 2026-05-16

- **Upstream Bump**: Updated base Bambuddy image to `0.2.4.1`

## [0.2.4-1] - 2026-05-16

- **Fix**: Reverted Home Assistant API URL to properly route notification service calls.
- **Auto-Discovery**: Added `bashio::services` integration to auto-discover MQTT broker credentials from Home Assistant if left as defaults in the UI config.

## [0.2.4] - 2026-05-15

- **Networking**: Switched to `host_network: true` to support SSDP discovery and Virtual Printer FTP file transfers.
- **Home Assistant API**: Seamlessly injected via Supervisor token (no manual UI setup required).
- **MQTT**: Added complete configurable integration with local Mosquitto brokers.
