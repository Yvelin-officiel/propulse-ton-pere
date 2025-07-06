FROM debian:bullseye-slim

WORKDIR /app

COPY simeis-server/target/release/simeis-server /app/simeis-server

RUN chmod +x /app/simeis-server

ENTRYPOINT ["/app/simeis-server"]
