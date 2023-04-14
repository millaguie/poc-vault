FROM debian:stretch-slim

RUN apt update && \
    apt upgrade -y && \
    apt install -y curl bash wget gpg lsb-release ca-certificates apt-transport-https && \
    wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | tee /usr/share/keyrings/hashicorp-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/hashicorp.list && \
    apt update && \
    apt install vault && \
    apt clean && \
    apt autoremove

ADD operator /usr/local/bin/operator

entrypoint ["/usr/local/bin/operator"]


