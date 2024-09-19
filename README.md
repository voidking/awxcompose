# awxcompose
AWX Docker-Compose YAML

# Project Description
A simplified version of [Installing AWX 17.1.0](https://github.com/ansible/awx/blob/17.1.0/INSTALL.md).
The official AWX Docker-Compose installation method is too complicated, so it is simplified into this project.

# Pre-preparation
- Docker 19.03.15+
- Docker-Compose 2.11.1+

# Automatic installation method
Not yet completed
```bash
bash <(curl -sL https://raw.githubusercontent.com/voidking/awxcompose/main/install.sh)
```

# Manual installation method
1. Get the code
```bash
git clone https://github.com/voidking/awxcompose.git
```

2. Prepare AWX configuration
```bash
cp -r awxcompose/17.1.0/awx /opt/
cd /opt/awx
vim environment.sh # Modify username and password as needed
vim credentials.py # Modify username and password as needed
```

3. Start AWX
```bash
docker-compose pull
docker-compose up -d
```

4. Initialize the database
```bash
docker exec -it awx_web /var/lib/awx/venv/awx/bin/awx-manage migrate
```

5. Restart AWX
```bash
docker-compose down
docker-compose up -d
```

# TODO
- Automatically install scripts
- Support more awx versions


