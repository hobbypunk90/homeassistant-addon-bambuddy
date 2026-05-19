# Configuration

The Bambuddy Obico ML API is designed to run silently alongside Bambuddy.

## Add-on Options

### Network
* **Port (default 3333)**: The port the ML API server runs on. If you change this from `3333`, make sure to update the `obico_ml_url` setting in the main Bambuddy add-on configuration (or its Web UI) to match the new port, e.g., `http://core-bambuddy-obico-ml:YOUR_NEW_PORT`.

## Bambuddy Integration

Once this add-on is running, Bambuddy will automatically utilize it if the `obico_ml_url` setting is pointed to it. 
For Home Assistant Add-on users, the typical URL is:
`http://core-bambuddy-obico-ml:3333`

Bambuddy's internal polling logic uses the custom `/detect/` POST endpoint exposed by this sidecar, which allows it to receive failure snapshots with bounding boxes pre-drawn over the spaghetti or layer shifts, enhancing the notifications you receive in Home Assistant.

### MQTT Sensor Automations
When integrated with this Add-on wrapper, three Home Assistant MQTT Auto-Discovery binary sensors are automatically created for each printer: `obico_active`, `obico_failed`, and `obico_monitoring`. These allow you to build seamless automations (like triggering chamber lights) that perfectly handle printer pauses without causing strobe effects. See the main repository README for configuration details.
