# Vault PoC

This repo contains a proof of concept for a Vault deployment using docker-compose. It is not intended for production use.

This docker compose file will start a Vault server, a PostgreSQL database, an operator script that configures the Vault to manage the users of the database and a simple web application that connects to the database using a Vault role to get its credentials.

The idea of this PoC is to be very simple and easy to understand, so it is intentionally not doing some things that you would do in a real deployment.

Please feel free to read the code and play with it.

## Prerequisites

- Docker
- Docker Compose v2 (`docker compose`)

## Usage

### Start

```bash
docker compose up -d --build
```

You can check the logs with `docker compose logs -f`. After two minutes the password of the application container will expire, the health check will fail and the application will be restarted, on the restart the application will get a new password from Vault and continue to work.

### Token and credential lifetimes

| What | Lifetime | Set in |
|---|---|---|
| Database user that the application gets from Vault | 2 minutes (5 minutes max) | `default_ttl` and `max_ttl` in `operator/operator` |
| Vault token that the application uses to ask for database users | 168 hours (7 days) | `default_lease_ttl` in `docker-compose.yml` |
| Root token | Does not expire | Created by `vault operator init` |

The application does not renew its Vault token. After 7 days the token expires: on the next restart the application cannot get a database user and fails to start.

The operator creates the application token only on the first start. Restarting the stack does not create a new one. To get a new token, start again from zero (see below).

### Stop

```bash
docker compose down
```

### Vault UI

You can play with Vault using the UI.

The Vault UI is available at http://localhost:8200

To login, use the root token from the following command:

```bash
docker compose run --rm --no-deps --entrypoint cat operator /vault/secret.output
```

To start again from zero (new Vault, new database), remove the volumes:

```bash
docker compose down -v
```
