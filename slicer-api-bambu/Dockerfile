ARG BUILD_FROM=ghcr.io/maziggy/bambu-studio-api:latest
FROM ${BUILD_FROM}

ENV PORT=3001
ENV DATA_PATH=/share/bambuddy/slicer/bambu
ENV BUNDLED_PROFILES_PATH=/app/squashfs-root/resources/profiles/BBL

EXPOSE 3001

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:3001/health || exit 1

CMD ["node", "/app/dist/index.js"]
