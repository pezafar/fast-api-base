# =============================================================================
# FastAPI Template Makefile - 2025 Best Practices with UV
# =============================================================================

SHELL := /bin/bash
.DEFAULT_GOAL := help

# Project Configuration
# -----------------------------------------------------------------------------
PROJECT_NAME := fastapi-template
PYTHON_VERSION := 3.12
HOST := 0.0.0.0
PORT := 8080

# Colors for output
RED := \033[0;31m
GREEN := \033[0;32m
YELLOW := \033[0;33m
BLUE := \033[0;34m
NC := \033[0m # No Color

# =============================================================================
# PHONY Targets
# =============================================================================
.PHONY: help install install-dev sync update-deps run run-prod test test-watch lint format check pre-commit clean clean-all docker-build docker-run docker-down setup-hooks

# =============================================================================
# Help Target
# =============================================================================
help: ## Show this help message
	@printf "$(GREEN)$(PROJECT_NAME) - Available Commands$(NC)\n"
	@echo "============================================"
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make $(BLUE)<target>$(NC)\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  $(BLUE)%-15s$(NC) %s\n", $$1, $$2 } /^##@/ { printf "\n$(YELLOW)%s$(NC)\n", substr($$0, 5) }' $(MAKEFILE_LIST)

# =============================================================================
##@ 🔧 Development Setup
# =============================================================================

install: ## Install production dependencies
	@printf "$(GREEN)Installing production dependencies...$(NC)\n"
	@uv sync --no-dev --frozen


install-dev: setup-env ## Install all dependencies including development tools
	@printf "$(GREEN)Installing all dependencies...$(NC)\n"
	@uv sync

setup-env: ## Setup development environment
	@printf "$(GREEN)Setting up development environment...$(NC)\n"
	@if [ ! -f .env ]; then \
		printf "$(YELLOW)Creating .env from .env.example...$(NC)\n"; \
		cp .env.example .env; \
	fi
	@uv python install $(PYTHON_VERSION) 2>/dev/null || printf "$(YELLOW)Python $(PYTHON_VERSION) already installed$(NC)\n"

sync: ## Sync dependencies with lockfile
	@printf "$(GREEN)Syncing dependencies...$(NC)\n"
	@uv sync

update-deps: ## Update all dependencies
	@printf "$(GREEN)Updating dependencies...$(NC)\n"
	@uv lock --upgrade

# =============================================================================
##@ 🚀 Running
# =============================================================================

run: 
	@printf "$(GREEN)Starting development server on http://$(HOST):$(PORT)$(NC)\n"
	@uv run uvicorn app.__main__:app --reload --host $(HOST) --port $(PORT)

run-prod: install ## Run production server
	@printf "$(GREEN)Starting production server...$(NC)\n"
	@uv run uvicorn app.__main__:app --host $(HOST) --port $(PORT) --workers 4

# =============================================================================
##@ 🧪 Testing
# =============================================================================

test: 
	@printf "$(GREEN)Running tests...$(NC)\n"
	@uv run pytest tests/ -v --tb=short

test-watch: 
	@printf "$(GREEN)Running tests in watch mode...$(NC)\n"
	@uv run pytest-watch tests/ -- -v --tb=short

test-cov: 
	@printf "$(GREEN)Running tests with coverage...$(NC)\n"
	@uv run pytest tests/ --cov=app --cov-report=html --cov-report=term-missing

# =============================================================================
##@ 🔍 Code Quality
# =============================================================================

lint: 
	@printf "$(GREEN)Running linting tools...$(NC)\n"
	@printf "$(BLUE)Running ruff check...$(NC)\n"
	@uv run ruff check .
	@printf "$(BLUE)Running ruff format check...$(NC)\n"
	@uv run ruff format --check .
	@printf "$(BLUE)Running pyright...$(NC)\n"
	@uv run pyright

format: 
	@printf "$(GREEN)Formatting code...$(NC)\n"
	@uv run ruff format .
	@uv run ruff check . --fix

check: lint test ## Run all checks (lint + test)

pre-commit: format check ## Run pre-commit checks
	@printf "$(GREEN)✅ All pre-commit checks passed!$(NC)\n"

setup-hooks: 
	@printf "$(GREEN)Setting up git hooks...$(NC)\n"
	@echo '#!/bin/bash\nmake pre-commit' > .git/hooks/pre-commit
	@chmod +x .git/hooks/pre-commit
	@printf "$(GREEN)Git hooks setup complete!$(NC)\n"

# =============================================================================
##@ 🐳 Docker
# =============================================================================

docker-build: ## Build Docker image
	@printf "$(GREEN)Building Docker image...$(NC)\n"
	@docker build -t $(PROJECT_NAME) .

docker-run: 
	@printf "$(GREEN)Running Docker container...$(NC)\n"
	@docker run -p $(PORT):$(PORT) --env-file .env $(PROJECT_NAME)

docker-compose-up: ## Start services with docker-compose
	@printf "$(GREEN)Starting services with docker-compose...$(NC)\n"
	@docker-compose up -d

docker-compose-down: ## Stop services with docker-compose
	@printf "$(GREEN)Stopping services with docker-compose...$(NC)\n"
	@docker-compose down

# =============================================================================
##@ 🧹 Cleanup
# =============================================================================

clean: ## Clean temporary files and caches
	@printf "$(GREEN)Cleaning temporary files...$(NC)\n"
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -delete
	@find . -type d -name "*.egg-info" -exec rm -rf {} +
	@find . -type d -name ".pytest_cache" -exec rm -rf {} +
	@find . -type f -name ".coverage" -delete
	@find . -type d -name "htmlcov" -exec rm -rf {} +
	@find . -type d -name ".ruff_cache" -exec rm -rf {} +
	@find . -type d -name ".mypy_cache" -exec rm -rf {} +

clean-all: clean ## Clean everything including virtual environment
	@printf "$(YELLOW)Removing virtual environment...$(NC)\n"
	@rm -rf .venv
	@printf "$(GREEN)Full cleanup complete!$(NC)\n"
