# Vault PoC

This repo contains a proof of concept for a Vault deployment using docker-compose. It is not intended for production use.

This docker compose file will start a Vault server, a PostgreSQL database, an operator script that configures the Vault to manage the users of the database and a simple web application that connects to the database using a Vault role to get its credentials.

The idea of this PoC is to be very simple and easy to understand, so it is intentionally not doing some things that you would do in a real deployment.

Please feel free to read the code and play with it.

## Prerequisites

- Docker
- Docker Compose

## Usage

### Start

```bash
docker-compose up -d
```

You can check the logs with `docker-compose logs -f`. After two minutes the password of the application container will expire, the health check will fail and the application will be restarted, on the restart the application will get a new password from Vault and continue to work.

### Stop

```bash
docker-compose down
```

### Vault UI

You can play with Vault using the UI.

The Vault UI is available at http://localhost:8200

To login, use the root token from the following command:

```bash
sudo cat $(docker volume inspect vault_vault-secrets | jq -r ".[0].Mountpoint")/secret.output
```
