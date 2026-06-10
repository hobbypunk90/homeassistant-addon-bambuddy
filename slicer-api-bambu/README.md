# Bambuddy Slicer API (Bambu)

A headless Bambu Studio API sidecar container for Bambuddy Auto-Slicing.

This Home Assistant add-on wraps `ghcr.io/maziggy/orca-slicer-api` (bambu variant) so it can be run as a sidecar alongside the Bambuddy add-on.
## Configuration

1. Start this add-on. Make sure port `3001` is exposed in the network settings.
2. In your Bambuddy add-on's Web UI, go to **Settings → Workflow → Slicer**.
3. Turn on **Use Slicer API**.
4. Set the **Sidecar URL** to `http://localhost:3001` (since Bambuddy runs on host networking).

## Persistent Data
Slicer API sidecars are completely stateless. They do not save any files or store any data between reboots. As such, they do not create any folders or expose any files to your Home Assistant `/share` directory. All persistent data (like your customized slicing presets) are stored securely by the main Bambuddy application in its SQLite database.
