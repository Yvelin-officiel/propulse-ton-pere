FROM debian:bullseye-slim

WORKDIR /app

COPY target/release/simeis-server.exe /app/simeis-server

RUN chmod +x /app/simeis-server

ENTRYPOINT ["/app/simeis-server"]
