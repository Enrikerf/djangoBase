.DEFAULT_GOAL := help

## —— 📦 Makefile 📦 —————————————————————————————————————————

help: ## Outputs this help screen
	@grep -E '(^[a-zA-Z0-9_-]+:.*?##.*$$)|(^##)' Makefile | awk 'BEGIN {FS = ":.*?## "}{printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'

## —— 🐋 Docker 🐋 —————————————————————————————————————————

up:
	docker-compose up -d
build:
	docker-compose build
down:
	docker-compose down
enter:
	docker exec -u docker-user -ti api /usr/bin/fish
enter_bash:
	docker exec -it api /bin/bash
@:
	help