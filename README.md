<p align="center">
  <img src="https://github.com/hobbypunk90/homeassistant-addon-bambuddy/blob/main/logo.png?raw=true" alt="Bambuddy Logo" width="300">
</p>

<h1 align="center">Bambuddy</h1>

<p align="center">
  <strong>Self-hosted print archive and management system for Bambu Lab 3D printers</strong>
</p>

<p align="center">
  <a href="https://github.com/maziggy/bambuddy/releases"><img src="https://img.shields.io/github/v/release/maziggy/bambuddy?style=flat-square&color=blue" alt="Release"></a>
  <img src="https://github.com/maziggy/bambuddy/actions/workflows/github-code-scanning/codeql/badge.svg">
  <img src="https://github.com/maziggy/bambuddy/actions/workflows/ci.yml/badge.svg?branch=main">  
  <a href="https://github.com/maziggy/bambuddy/blob/main/LICENSE"><img src="https://img.shields.io/github/license/maziggy/bambuddy?style=flat-square" alt="License"></a>
  <a href="https://github.com/maziggy/bambuddy/stargazers"><img src="https://img.shields.io/github/stars/maziggy/bambuddy?style=flat-square" alt="Stars"></a>
  <a href="https://github.com/maziggy/bambuddy/issues"><img src="https://img.shields.io/github/issues/maziggy/bambuddy?style=flat-square" alt="Issues"></a>
  <a href="https://discord.gg/aFS3ZfScHM"><img src="https://img.shields.io/discord/1461241694715645994?style=flat-square&logo=discord&logoColor=white&label=Discord&color=5865F2" alt="Discord"></a>
  <a href="https://ko-fi.com/maziggy"><img src="https://img.shields.io/badge/Ko--fi-Support-ff5e5b?style=flat-square&logo=ko-fi&logoColor=white" alt="Ko-fi" target=_blank></a>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-screenshots">Screenshots</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="http://wiki.bambuddy.cool">Documentation</a> •
  <a href="https://discord.gg/aFS3ZfScHM">Discord</a> •
  <a href="#-contributing">Contributing</a>
</p>

---

## Why Bambuddy?

- **Own your data** — All print history stored locally, no cloud dependency
- **Works offline** — Uses Developer Mode for direct printer control via local network
- **Full automation** — Schedule prints, auto power-off, get notified when done
- **Multi-printer support** — Manage your entire print farm from one interface

---

## ✨ Features

<table>
<tr>
<td width="50%" valign="top">

### 📦 Print Archive

- Automatic 3MF archiving with metadata
- 3D model preview (Three.js)
- Duplicate detection & full-text search
- Photo attachments & failure analysis
- Timelapse editor (trim, speed, music)
- Re-print to any connected printer with AMS mapping (auto-match or manual slot selection, multi-plate support)
- Plate thumbnail browsing for multi-plate archives (hover to navigate between plates)
- Archive comparison (side-by-side diff)
- Tag management (rename/delete across all archives)

### 📊 Monitoring & Control

- Real-time printer status via WebSocket
- Live camera streaming (MJPEG) & snapshots with multi-viewer support
- **Streaming overlay for OBS** - Embeddable page with camera + status for live streaming (`/overlay/:printerId`), configurable FPS (`?fps=30`), status-only mode (`?camera=false`)
- External camera support (MJPEG, RTSP, HTTP snapshot, USB/V4L2) with layer-based timelapse
- **Build plate empty detection** - Auto-pause print if objects detected on plate (multi-reference calibration, ROI adjustment)
- Fan status monitoring (part cooling, auxiliary, chamber)
- Printer control (stop, pause, resume, chamber light)
- Resizable printer cards (S/M/L/XL)
- Skip objects during print
- AMS slot RFID re-read
- AMS slot configuration (custom presets, K profiles, color picker)
- HMS error monitoring with history
- Print success rates & trends
- Filament usage tracking
- Cost analytics & failure analysis
- CSV/Excel export

### ⏰ Scheduling & Automation

- Print queue with drag-and-drop
- Multi-printer selection (send to multiple printers at once)
- Model-based queue assignment (send to "any X1C" for load balancing) with location filtering
- Filament validation (only assign to printers with required filaments)
- Per-printer AMS mapping (individual slot configuration for print farms)
- Scheduled prints (date/time)
- Queue Only mode (stage without auto-start)
- Smart plug integration (Tasmota, Home Assistant, MQTT)
- MQTT smart plugs: Subscribe to Zigbee2MQTT, Shelly, or any MQTT topic for energy monitoring
- Energy consumption tracking (per-print kWh and cost)
- HA energy sensor support (for plugs with separate power/energy sensors)
- Auto power-on before print
- Auto power-off after cooldown

### 📁 File Manager (Library)

- Upload and organize sliced files (3MF, gcode, STL)
- **STL thumbnail generation** - Auto-generate previews for STL files on upload or batch generate for existing files
- ZIP file extraction with folder structure preservation
- Option to create folder from ZIP filename
- Folder structure with drag-and-drop
- Rename files and folders via context menu
- Print directly to any printer with full options
- Add to queue without creating archive upfront
- Plate selection for multi-plate 3MF files
- Duplicate detection via file hash
- Mobile-friendly with always-visible action buttons

### 📁 Projects

- Group related prints (e.g., "Voron Build")
- Track plates (print jobs) and parts separately
- Auto-detect parts count from 3MF files
- Color-coded project badges
- Bulk assign archives via multi-select toolbar
- Import/Export projects as ZIP (includes files) or JSON

</td>
<td width="50%" valign="top">

### 🔔 Notifications

- WhatsApp, Telegram, Discord
- Email, Pushover, ntfy
- Custom webhooks
- Quiet hours & daily digest
- Customizable message templates
- Print finish photo URL in notifications
- HMS error alerts (AMS, nozzle, etc.)
- Build plate detection alerts
- Queue events (waiting, skipped, failed)

### 🔧 Integrations

- [Spoolman](https://github.com/Donkie/Spoolman) filament sync
- MQTT publishing for Home Assistant, Node-RED, etc.
- **Prometheus metrics** - Export printer telemetry for Grafana dashboards
- Bambu Cloud profile management
- K-profiles (pressure advance)
- **GitHub backup** - Schedule automatic backups of cloud profiles, k profiles and settings to GitHub
- External sidebar links
- Webhooks & API keys
- Interactive API browser with live testing

### 🖨️ Virtual Printer & Remote Printing

- **🌐 Proxy Mode (NEW!)** — Print remotely from anywhere via secure TLS relay
- Emulates a Bambu Lab printer on your network
- Send prints directly from Bambu Studio/Orca Slicer
- Configurable printer model (X1C, P1S, A1, H2D, etc.)
- Archive mode, Review mode, Queue mode, or Proxy mode
- SSDP discovery (appears in slicer automatically)
- Secure TLS/MQTT/FTP communication

### 🛠️ Maintenance & Support

- Maintenance scheduling & tracking
- Interval reminders (hours/days)
- Print time accuracy stats
- File manager for printer storage
- Firmware update helper (LAN-only printers)
- Debug logging toggle with live indicator
- Live application log viewer with filtering
- Support bundle generator (privacy-filtered)

### 🔒 Optional Authentication

- Enable/disable authentication any time
- Group-based permissions (50+ granular permissions)
- Default groups: Administrators, Operators, Viewers
- JWT tokens with secure password hashing
- Comprehensive API protection (200+ endpoints secured)
- User management (create, edit, delete, groups)
- User activity tracking (who uploaded archives, library files, queued prints, started prints)

</td>
</tr>
</table>

**Plus:** Customizable themes (style, background, accent) • Mobile responsive • Keyboard shortcuts • Multi-language (EN/DE) • Auto updates • Database backup/restore • System info dashboard

## 🖨️ Supported Printers

| Series | Models |
|--------|--------|
| H2 | H2D, H2S |
| X1 | X1, X1 Carbon |
| P1 | P1P, P1S, P2S |
| A1 | A1, A1 Mini |

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Backend | Python, FastAPI, SQLAlchemy |
| Frontend | React, TypeScript, Tailwind CSS |
| Database | SQLite |
| 3D Viewer | Three.js |
| Communication | MQTT (TLS), FTPS |

---

## 🤝 Contributing

Contributions welcome! Here's how to help:

1. **Test** — Report issues with your printer model
2. **Translate** — Add new languages
3. **Code** — Submit PRs for bugs or features
4. **Document** — Improve wiki and guides

```bash
# Development setup
git clone https://github.com/maziggy/bambuddy.git
cd bambuddy

# Backend
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
DEBUG=true uvicorn backend.app.main:app --reload

# Frontend (separate terminal)
cd frontend && npm install && npm run dev
```

See [CONTRIBUTING.md](https://github.com/maziggy/bambuddy/blob/main/CONTRIBUTING.md) for guidelines.

---

## 📄 License

MIT License — see [LICENSE](https://github.com/maziggy/bambuddy/blob/main/LICENSE) for details.

---

## 🙏 Acknowledgments

- [Bambu Lab](https://bambulab.com/) for amazing printers
- The reverse engineering community for protocol documentation
- All testers and contributors

---

If you like Bambuddy and want to support it, you can <a href="https://ko-fi.com/maziggy" target=_blank>buy Martin a coffee</a>.

---

<p align="center">
  Made with ❤️ for the 3D printing community
  <br><br>
  <a href="https://discord.gg/aFS3ZfScHM">Join our Discord</a> •
  <a href="https://github.com/maziggy/bambuddy/issues">Report Bug</a> •
  <a href="https://github.com/maziggy/bambuddy/issues">Request Feature</a> •
  <a href="http://wiki.bambuddy.cool">Documentation</a>
</p>
