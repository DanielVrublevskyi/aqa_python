FROM jenkins/jenkins:lts-jdk21

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3 python3-pip python3-venv libatomic1 && \
    python3 -m venv /tmp/pw-setup && \
    /tmp/pw-setup/bin/pip install playwright==1.65.2 && \
    /tmp/pw-setup/bin/python -m playwright install-deps chromium && \
    rm -rf /tmp/pw-setup /var/lib/apt/lists/*

USER jenkins