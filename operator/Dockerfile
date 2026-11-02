ARG VAULT_IMAGE=hashicorp/vault:2.2.1
FROM ${VAULT_IMAGE}

USER root
RUN apk add --no-cache bash curl

COPY operator /usr/local/bin/operator

ENTRYPOINT ["/usr/local/bin/operator"]
