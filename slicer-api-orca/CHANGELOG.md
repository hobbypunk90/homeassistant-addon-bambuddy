# Changelog

All notable changes to the App will be documented in this file.

## [2.3.2.1] - 2026-06-10
- **Pre-compiled Images**: The add-on now pulls directly from the pre-built `ghcr.io/maziggy/orca-slicer-api` image instead of compiling from source. This eliminates build failures on platforms lacking Git/BuildKit and dramatically speeds up installation.

## [2.3.2] - 2026-06-09
- **Upstream Sync**: Adopted consistent versioning scheme matching the underlying OrcaSlicer version (`2.3.2`).

## [1.1] - 2026-05-15
- Initial stable release of the dedicated Slicer API sidecar container.
