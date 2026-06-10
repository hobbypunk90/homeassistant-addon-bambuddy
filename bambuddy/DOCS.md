# Bambuddy Home Assistant Add-on

## Configuration Options

This add-on provides several configuration options to customize your Bambuddy experience. Most users can leave these at their default values.

### Auto-Slicing Configuration
If you want to use the automated print queuing and slicing features, you must install the accompanying Slicer API add-ons provided in the same repository as Bambuddy:
*   **Slicer API - Orca** (Slug: `bambuddy_orca_slicer_api`)
*   **Slicer API - Bambu** (Slug: `bambuddy_bambu_studio_api`)

Because Bambuddy runs in `host_network` mode, it communicates with these sidecars locally through the host machine rather than the internal Docker bridge network. The default configurations are pre-populated and ready to use without requiring internal DNS names:
*   **`orcaslicer_api_url`**: `http://127.0.0.1:3003`
*   **`bambu_studio_api_url`**: `http://127.0.0.1:3001`
*   **`preferred_slicer`**: Select which slicer engine you want Bambuddy to use by default.

### Security
*   **`mfa_encryption_key`**: A 32-character string used to encrypt the MFA database. Leave blank for default internal security, or define your own for maximum security.

### Database
*   **`database_url`**: By default, Bambuddy creates a local `bambuddy.db` file in your `/share/bambuddy/data` folder. If you are a power user and want to connect to an external PostgreSQL database for high availability, enter the connection string here (e.g., `postgresql+asyncpg://user:pass@192.168.1.50/bambuddy`). Otherwise, **leave this blank**.

### Virtual Printer Configuration
*   **`virtual_printer_pasv_address`**: Bambuddy can emulate a physical printer to trick Bambu Studio/OrcaSlicer into sending files to it directly. This emulation uses the FTP protocol. Passive FTP (PASV) requires the server to tell the client what IP address to use for the data connection. 
    *   If Bambuddy is running behind complex routing, you may need to explicitly tell it your Home Assistant machine's IP address (e.g., `192.168.1.100`) so it hands out the correct IP to your slicer software. 
    *   For most flat local networks, you can **leave this blank**.

### MQTT Relay Settings
Bambuddy connects directly to your printer to monitor it, but it can also "Relay" these events (Print Started, Filament Low, etc.) to your Home Assistant MQTT broker so you can build automations around them.

**If you use the official Mosquitto Add-on, MQTT works automatically with no configuration needed.** The add-on auto-discovers broker credentials from the Supervisor on first startup.

We have removed the manual MQTT configuration fields from the HAOS Add-on config tab to prevent confusion and bugs. If you need to override the auto-discovered settings (or set up an external broker manually), you must do so from inside the **Bambuddy App Web UI** (`Settings` > `Integrations` > `MQTT`). 

Any manual edits made inside the Bambuddy App UI will permanently override the HAOS auto-discovery and persist across restarts. To verify your MQTT connection is successful, check the status indicator inside the Bambuddy App settings page.

### Network Ports (Advanced)
Because Bambuddy relies on emulating physical Bambu Lab printer hardware to capture print jobs via the "Virtual Printer" feature, it must run in `host_network` mode. This means it binds directly to your Home Assistant host's network interfaces.

It uses the following ports internally. **If you have other Add-ons using these ports, Bambuddy's Virtual Printer feature may fail to start:**
*   **8000 (TCP)**: The Bambuddy Web UI.
*   **8883 (TCP)**: MQTT Status Stream (Conflicts with Mosquitto Add-on if TLS is enabled on default port. You may need to change Mosquitto's SSL port to 18883/18884).
*   **3000 & 3002 (TCP)**: Virtual Printer Handshake / Slicer proxy (Conflicts with Z-Wave JS UI. You must change Z-Wave JS UI's host port if installed).
*   **322 & 6000 (TCP)**: RTSP Camera streaming ports.
*   **990 (TCP) & 50000-50100 (TCP)**: FTPS server and dynamic file upload ports. 
*   **2021 (UDP)**: Virtual Printer SSDP / mDNS auto-discovery broadcast.

### Persistent Data & Custom Presets
The Bambuddy add-on uses Home Assistant's `/addon_configs` and `/share` directories to safely store its database and user data so that it persists across reboots and add-on updates.

**⚠️ Pre-Update Backup Warning (v0.2.4.5)**: If you are upgrading and you access your `/share/bambuddy` files from an external device/sync, or if you previously mounted external folders into Bambuddy, we strongly recommend creating a full backup before updating!

You can access these files via the **Samba Share** add-on or the **Advanced SSH** add-on at:
*   `/addon_configs/bambuddy-dev/data/bambuddy.db` - Your persistent SQLite database containing all print history, stats, and settings. This is kept out of the main `share` folder for security.
*   `/addon_configs/bambuddy-dev/logs/` - Diagnostic logs.
*   `/share/bambuddy/archive/` - Your user-facing print archives and 3D models.
*   `/share/bambuddy/backups/` - Auto-generated `.zip` backups of your database.

### External Storage & File Manager
If you want to use the Bambuddy File Manager to browse other shared folders on your Home Assistant machine (e.g., a NAS mounted to `/share/nas_drive`), you must explicitly allow them:
*   **`bambuddy_external_roots`**: A colon-separated list of paths the File Manager is allowed to see (e.g., `/share/nas_drive:/share/external_models`). For security, upstream Bambuddy hard-rejects its own data directory, so you **cannot** use `/share/bambuddy` as an external root.

**Importing Custom Presets:**
To import custom filament or slicing presets into Bambuddy, you do **not** need to manually drop files into the `/share` folder. Simply open the **Bambuddy Web UI**, navigate to the **Presets** or **Library** section, and use the built-in upload/import tools to add your custom `.json` or `.3mf` presets. Because the database is safely mapped to the `/share` folder, your imported profiles will be permanently saved.

---
## Support
If you have issues, please check the `/share/bambuddy/logs` directory via your Home Assistant File editor or Samba share.
