FROM debian:bullseye-slim

WORKDIR /app

COPY target/release/simeis-server /app/simeis-server

RUN chmod +x /app/simeis-server

CMD ["/app/simeis-server"]
