ARG BUILD_FROM=ghcr.io/maziggy/orca-slicer-api:latest
FROM ${BUILD_FROM}

ENV PORT=3003
ENV DATA_PATH=/share/bambuddy/slicer/orca

EXPOSE 3003

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:3003/health || exit 1

CMD ["node", "/app/dist/index.js"]
