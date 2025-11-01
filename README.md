# FastAPI Template
Fast api simple template.
Package management with uv, code quality with ruff and pyright.
Based on [cookiecutter-fastapi repo](https://github.com/arthurhenrique/cookiecutter-fastapi)

## Development Requirements

- Python 3.9+
- [UV](https://docs.astral.sh/uv/) (Python Package Manager)

## Quick Start

```sh
# Get help with all available commands
make help

# Install development dependencies
make install-dev

# Run the development server
make run

# Run tests
make test

# Check code quality
make check
```

## 📋 Available Commands

Run `make help` to see all project commands.

## Development Workflow

1. **Initial Setup**:
   ```sh
   make install-dev
   make setup-hooks  # Optional: setup git hooks
   ```

2. **Daily Development**:
   ```sh
   make run          # Start development server
   make test-watch   # Run tests in another terminal
   ```

3. **Before Committing**:
   ```sh
   make pre-commit   # Format code and run all checks
   ```

4. **Update Dependencies**:
   ```sh
   make update-deps  # Update all dependencies
   make sync         # Sync with updated lockfile
   ```

## Access Documentation

- **Swagger UI**: <http://localhost:8080/docs>
- **ReDoc**: <http://localhost:8080/redoc>

## Project Structure

Files related to application are in the `app` or `tests` directories.

```
app/
├── api/                 # Web related stuff
│   └── routes/          # API routes and endpoints
├── core/                # Application configuration, startup events, logging
├── models/              # Pydantic models for this application
├── services/            # Business logic and service layer
└── __main__.py          # FastAPI application creation and configuration

tests/                   # Test files using pytest
├── test_api_*.py        # API endpoint tests
├── test_*_service.py    # Service layer tests
└── test_*.py            # Other unit tests

# Configuration files
├── pyproject.toml       # Project dependencies and configuration
├── uv.lock              # Locked dependency versions
├── Makefile             # Development commands
├── Dockerfile           # Docker container configuration
├── docker-compose.yml   # Multi-service Docker setup
└── .env.example         # Environment variables template
```

## Configuration

The application uses environment variables for configuration. Copy `.env.example` to `.env` and modify as needed:

```sh
cp .env.example .env
```

Key environment variables:
- `DEBUG`: Enable debug mode (default: false)
- `PROJECT_NAME`: Application name
- `DATABASE_URL`: Database connection string
- `SECRET_KEY`: Secret key for authentication

## Authentication

The template includes a simple Bearer token authentication system. In production, replace this with a proper JWT implementation or OAuth2.

Default token for development: `123`

Example API call:
```sh
curl -H "Authorization: Bearer 123" http://localhost:8080/api/v1/items
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Run quality checks: `make pre-commit`
5. Commit your changes: `git commit -m "Description"`
6. Push to the branch: `git push origin feature-name`
7. Submit a pull request


