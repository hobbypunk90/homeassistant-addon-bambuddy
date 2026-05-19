# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
ARG BAMBUDDY_VERSION="0.2.4.1"
ARG BUILD_ARCH
ARG BUILD_FROM="ghcr.io/home-assistant/${BUILD_ARCH}-base-python:3.11-alpine3.21"

FROM ghcr.io/maziggy/bambuddy:${BAMBUDDY_VERSION} AS builder
FROM $BUILD_FROM

LABEL \
  org.opencontainers.image.title="Home Assistant Add-on: Bambuddy add-on" \
  org.opencontainers.image.description="A powerful, self-hosted print archive and management system for Bambu Lab 3D printers." \
  org.opencontainers.image.source="https://github.com/connormxy/homeassistant-addon-bambuddy" \
  org.opencontainers.image.licenses="MIT License"

WORKDIR /app

# Install system dependencies
# NOTE: py3-opencv is NOT used — it installs cv2 into Alpine's system Python,
# but HA's Python lives in /usr/local and never sees it. Instead we pip-install
# opencv-python-headless from HA's precompiled musllinux wheels below.
RUN apk add --no-cache \
  build-base \
  curl \
  ffmpeg \
  libstdc++ \
  libjpeg-turbo \
  libpng \
  tiff \
  libwebp

# Install Python dependencies with cache mount
# --find-links pulls prebuilt musllinux wheels (including opencv-python-headless)
# from Home Assistant's wheel server so nothing compiles from source.
COPY --from=builder /app/requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
  pip install --root-user-action=ignore --upgrade pip \
  && echo "numpy<2" > /tmp/constraints.txt \
  && pip install --root-user-action=ignore \
     --find-links https://wheels.home-assistant.io/musllinux/ \
     --prefer-binary \
     -c /tmp/constraints.txt \
     -r requirements.txt

COPY --from=builder /app /app

# Patch notification_service.py to support HA 2024.6 notify entities
COPY notification_service.patch /app/notification_service.patch
RUN patch -p1 -d /app < /app/notification_service.patch && rm /app/notification_service.patch

# Patch Obico ML detection logic to support rich bounding box notifications
COPY obico_bounding_box.patch /app/obico_bounding_box.patch
RUN patch -p1 -d /app < /app/obico_bounding_box.patch && rm /app/obico_bounding_box.patch

# Patch Obico MQTT payload and resilient monitoring states
COPY obico_monitoring_mqtt.patch /app/obico_monitoring_mqtt.patch
RUN patch -p1 -d /app < /app/obico_monitoring_mqtt.patch && rm /app/obico_monitoring_mqtt.patch

ENV PYTHONUNBUFFERED=1
ENV DATA_DIR=/app/data
ENV LOG_DIR=/app/logs

# Copy root filesystem
COPY rootfs /
