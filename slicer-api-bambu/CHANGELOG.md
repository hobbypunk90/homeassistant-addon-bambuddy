# Changelog

All notable changes to the App will be documented in this file.

## [02.07.01.57.1] - 2026-06-10
- **Pre-compiled Images**: The add-on now pulls directly from the pre-built `ghcr.io/maziggy/bambu-studio-api` image instead of compiling from source. This eliminates build failures on platforms lacking Git/BuildKit and dramatically speeds up installation.

## [02.07.01.57] - 2026-06-09
- **Upstream Bump**: Updated Bambu Studio base image to version `02.07.01.57` for compatibility with Bambuddy 0.2.4.5.
- **Ubuntu Migration**: Switched the base OS to Ubuntu 22.04 and updated `libwebkit2gtk-4.1-0` to match upstream changes to the AppImage.

## [1.1] - 2026-05-15
- Initial stable release of the dedicated Slicer API sidecar container.
