<p align="center">
  <img src="https://github.com/connormxy/homeassistant-addon-bambuddy/blob/main/bambuddy/logo.png?raw=true" alt="Bambuddy Logo" width="300">
</p>

# Bambuddy – Home Assistant Add-on Repository

[Bambuddy](https://github.com/maziggy/bambuddy) wrapped inside a Home Assistant add-on, with companion Slicer API sidecars.

A self-hosted print archive and management system for Bambu Lab 3D printers.

![Supports aarch64 Architecture][aarch64-shield] ![Supports amd64 Architecture][amd64-shield] ![Supports armhf Architecture][armhf-shield] ![Supports armv7 Architecture][armv7-shield] ![Supports i386 Architecture][i386-shield]

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg

---

## What This Add-on Provides

This repository delivers a **multi-app ecosystem** for running Bambuddy on Home Assistant OS with minimal setup:

### 🧩 Four Installable Add-ons
| Add-on | Port | Purpose |
|--------|------|---------|
| **Bambuddy** | 8000 | Core application — printer monitoring, archive, queue, notifications |
| **Slicer API (Bambu Studio)** | 3001 | Optional headless slicing sidecar for Bambu Studio files |
| **Slicer API (OrcaSlicer)** | 3003 | Optional headless slicing sidecar for OrcaSlicer files |
| **Obico ML API** | 3333 | Optional headless ML sidecar for AI failure detection |

Install the main add-on **and** any optional sidecars you need.

### 🔌 Zero-Config Home Assistant Integration
- **API connectivity** is automatic — the Supervisor injects the HA URL and token at startup, enabling HA notifications (including 2024.6+ `notify.send_message` entities) with no manual setup.
- **MQTT auto-discovery** — If the [Mosquitto add-on](https://github.com/home-assistant/addons/tree/master/mosquitto) is installed, broker credentials are auto-detected from the Supervisor. MQTT just works. You can override any setting in the add-on config or the Bambuddy web UI.
- **Timezone** is automatically injected by the Supervisor.

### 🖼️ Empty Plate Detection (OpenCV)
The Docker image uses a **Python 3.11 base** specifically tailored to match Home Assistant's precompiled [`opencv-python-headless`](https://wheels.home-assistant.io/musllinux/) wheels. This means:
- **~5 minute install** instead of a 30+ minute source compilation that usually fails
- Empty plate detection works out of the box

### 🤖 AI Failure Detection (Obico ML)
Bambuddy can monitor your print's camera feed in real-time and detect failures (spaghetti, layer shifts, etc.) via a self-hosted Obico ML server. To enable this, simply install the **Obico ML API** add-on provided in this repository alongside Bambuddy. *(Note: The Obico ML add-on is heavily based on the excellent work by [nobodyguy](https://github.com/nobodyguy/obico_ml_ha_addon)).*

> **Note:** This is useful for **all** Bambu printers. While some models (X1C, P1S) have built-in lidar for first-layer inspection, continuous AI print monitoring is a Bambu Cloud feature that is **not available in developer/LAN mode**. Obico ML fills that gap locally.

The included **Obico ML API** add-on exposes a customized endpoint (`/detect/`) that automatically draws visual bounding boxes around detected failures, passing them directly into Bambuddy's Home Assistant push notifications so you can easily see what went wrong.

**Smart Chamber Light Automations:**
This Home Assistant Add-on wrapper enhances Bambuddy by injecting three MQTT **auto-discovery binary sensors** for the Obico ML integration. They will automatically appear under your printer's MQTT device in HA, allowing you to build clean automations (like controlling chamber lights) without worrying about strobe effects during print pauses:
- `binary_sensor.bambuddy_<serial>_obico_active`: ON ONLY while actively checking photos (turns off immediately when paused).
- `binary_sensor.bambuddy_<serial>_obico_failed`: ON ONLY if a spaghetti failure is currently latched (stays true during the pause, clears on resume).
- `binary_sensor.bambuddy_<serial>_obico_monitoring`: ON if Obico is active OR a failure is latched.

Use the unified `obico_monitoring` sensor as a single condition (`state == 'on'`) to seamlessly keep your lights on while the printer runs, and *stay on* while investigating a failure.

### 🔧 Configurable Slicer Endpoints
Default slicer URLs point to `http://127.0.0.1:3001` / `:3003` for the co-located sidecars. Override in the add-on config to point at remote slicer instances if needed.

### ⚠️ Host Network Mode
Bambuddy runs in `host_network: true` mode. This is **required** for:
- SSDP printer discovery
- Virtual Printer FTP file transfers
- Camera streaming

**Port conflict warning** — Bambuddy binds several ports on the host (8000, 8883, 3000, 3002, 322, 990, 2021, 6000, 50000–50100). Review the [DOCS.md](./bambuddy/DOCS.md) for the full list and check for conflicts with other add-ons (notably Z-Wave JS UI on port 3000, and Mosquitto TLS on 8883).

### 🚫 Ingress Not Supported
Bambuddy is accessed directly via its web UI at `http://<your-ha-ip>:8000` — it **cannot** run behind Home Assistant's ingress iframe proxy. The frontend uses fixed root-context paths and WebSocket connections that are incompatible with ingress's dynamic `/api/hassio_ingress/<token>/` URL rewriting. This would require significant upstream changes to Bambuddy's routing architecture.

---

## Installation

1. Add this repository URL to your Home Assistant add-on store:
   ```
   https://github.com/connormxy/homeassistant-addon-bambuddy
   ```
2. Install **Bambuddy** from the store.
3. (Optional) Install one or both **Slicer API** add-ons for auto-slicing.
4. Start the add-ons — MQTT and HA API are configured automatically.

## Configuration & Documentation

See the **Documentation** tab in the Home Assistant add-on page, or view [DOCS.md](./bambuddy/DOCS.md) for detailed explanations of:
- MQTT Relay Configuration
- Slicer API routing
- Database and Security overrides
- Virtual Printer Setup
- Port conflict resolution

---

<sub>The Home Assistant add-on wrapper code in this repository was developed with assistance from Claude (Anthropic) and Gemini (Google). All generated code was reviewed and tested by the maintainer.</sub>
