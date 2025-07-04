FROM debian:bookworm-slim

# Installer uniquement les dépendances d'exécution nécessaires (ex : libssl si ton binaire le requiert)
RUN apt-get update && apt-get install -y libssl-dev 

WORKDIR /app
# Copier uniquement le binaire compilé
COPY /target/release/simeis-server.exe .

EXPOSE 8080

ENTRYPOINT ["/usr/local/bin/simeis-server"]
