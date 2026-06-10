<!-- https://developers.home-assistant.io/docs/add-ons/presentation#keeping-a-changelog -->

# Changelog

All notable changes to the App will be documented in this file.

## [0.2.4.6.2] - 2026-06-10
**⚠️ We strongly recommend creating a full backup before updating. If you're upgrading from below 0.2.4.5, pay special attention if you access your `/share/bambuddy` files from an external device/sync, or if you previously mounted external folders into Bambuddy!**

- **Upstream Bump**: Updated base Bambuddy image to the latest `0.2.4.6`.
- **Breaking Change — Storage Overhaul**: The core database (`bambuddy.db`) and internal files have been moved out of the exposed `/share/bambuddy/data` directory and securely into `/addon_configs/bambuddy-dev/data/` (so it remains user-accessible, but is less easily exposed outside the machine via Samba/NAS). User-facing directories (`archive`, `firmware`, `virtual_printer`, `backups`) are now located directly in `/share/bambuddy/` and are natively symlinked. Existing installations will automatically migrate data to this new secure layout on the first start. **Users already accessing the `/share/bambuddy/data/` folder prior to update from external sites must ensure any external shares or syncs will not overwrite the new folder structure.**
- **Breaking Change — External Roots**: *ONLY for users already mounting "external folders" within bambuddy (NOT the default `/share/bambuddy` directory).* Upstream Bambuddy now hard-rejects its own data directories and requires explicit enumeration of any external folder the user might wish to mount. To continue using external library folders, you MUST configure the new `bambuddy_external_roots` option (a colon-separated list) in the Home Assistant Add-on config. Follow the specific rules for your external mounts before updating and restarting.
- **Slicer APIs Optimized**: Replaced the bulky, source-compiled Dockerfiles for the Orca and Bambu Slicer API add-ons. They now pull directly from the pre-built `ghcr.io/maziggy` images (`orca-slicer-api` and `bambu-studio-api`), eliminating build issues on architectures missing BuildKit/Container Station components.
- **Firmware Symlink**: Added the `firmware` folder to the `/share/bambuddy/` symlinks and migration logic so offline users can drop `.json` and `.swu` packages over SMB.
- **MQTT Zero-Config**: Removed manual MQTT overrides from the HAOS add-on config schema to prevent configuration conflicts. MQTT is strictly auto-discovered from the Supervisor on the first boot. Any manual edits made inside the Bambuddy App UI will still override auto-discovery and persist on restarts as intended.
- **API Access Flags Automigration**: Bambuddy will automigrate existing API access flags into the database on the first start.
- **Slicer Config Logic**: Fixed run script to correctly export `SLICER_API_URL` based on the user's preferred slicer addon configuration, matching upstream requirements.
- **Obico Patch Fixes**: Formatted and correctly encoded the `obico_bounding_box.patch`, `obico_monitoring_mqtt.patch`, and `notification_service.patch` files as perfect Git unified diffs to prevent `patch.exe` assertions and `exit code 2` errors during Docker build, fully enabling the Obico ML sidecar features.
- **UI Tweaks**: Hid advanced optional configuration settings (`bambuddy_external_roots`, `database_url`, `mfa_encryption_key`, `virtual_printer_pasv_address`) in the UI by default.

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
