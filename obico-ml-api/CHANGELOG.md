# Changelog

## 1.4-0.1.3
- **Bugfix**: Fixed a `Permission denied` (exit code 126) error that prevented the add-on from starting by ensuring `s6-overlay` startup scripts are properly marked as executable.

## 1.4-0.1.2
- **First Stable Release**
- Added `draw_bounding_boxes` configuration toggle to allow users to disable AI bounding boxes in snapshots if desired.

## 1.4-0.1
- Initial public release of the Bambuddy Obico ML API sidecar wrapper.
- Refactored build architecture for multi-arch compatibility (amd64, aarch64) matching standard Home Assistant paradigms.
