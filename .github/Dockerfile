FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y libssl-dev 

WORKDIR /app
# Copier uniquement le binaire compilé
COPY /target/release/simeis-server.exe .

EXPOSE 8080

ENTRYPOINT ["/usr/local/bin/simeis-server"]
