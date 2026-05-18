<!-- https://developers.home-assistant.io/docs/add-ons/presentation#keeping-a-changelog -->

# Changelog

All notable changes to the App will be documented in this file.

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
