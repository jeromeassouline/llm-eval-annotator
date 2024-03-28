# llm-eval-annotator

> Project to test tools to evaluate and annotate LLM responses

## Project requirements

### Pyenv and `Python 3.11.6`

- Install [pyenv](https://github.com/pyenv/pyenv) to manage your Python versions and virtual environments:
  ```bash
  curl -sSL https://pyenv.run | bash
  ```
  - If you are on MacOS and experiencing errors on python install with pyenv, follow this [comment](https://github.com/pyenv/pyenv/issues/1740#issuecomment-738749988)
  - Add these lines to your `~/.bashrc` or `~/.zshrc` to be able to activate `pyenv virtualenv`:
      ```bash
      eval "$(pyenv init -)"
      eval "$(pyenv virtualenv-init -)"
      eval "$(pyenv init --path)"
      ```
  - Restart your shell

- Install the right version of `Python` with `pyenv`:
  ```bash
  pyenv install 3.11.6
  ```

### Poetry

- Install [Poetry](https://python-poetry.org) to manage your dependencies and tooling configs:
  ```bash
  curl -sSL https://install.python-poetry.org | python - --version 1.7.0
  ```
  *If you have not previously installed any Python version, you may need to set your global Python version before installing Poetry:*
    ```bash
    pyenv global 3.11.6
    ```

### Docker Engine

Install [Docker Engine](https://docs.docker.com/engine/install/) to build and run the API's Docker image locally.

## Installation

### Python virtual environment and dependencies

1. Create a `pyenv` virtual environment and link it to your project folder:
    ```bash
    pyenv virtualenv 3.11.6 llm-eval-annotator
    pyenv local llm-eval-annotator
    ```
    *Now, every time you are in your project directory your virtualenv will be activated!*


2. Install dependencies with `Poetry`:
    ```bash
    poetry install --no-root
    ```

Steps 1. and 2. can also be done in one command:
```bash
make install
```

### Install git hooks (running before commit and push commands)

```bash
poetry run pre-commit install
```

### Pull data from DVC remote

- Make sure you have access to the DVC remote bucket (see bucket URL in `.dvc/config` file). If not, ask an administrator to give you access.
- Pull the data:
  ```bash
  dvc pull
  ```

## Testing

To run unit tests, run `pytest` with:
```bash
pytest tests --cov src
```
or
```bash
make test
```

## Formatting and static analysis

### Code formatting with `ruff`

To check code formatting, run `ruff format` with:
```bash
ruff format --check .
```
or
```bash
make format-check
```

You can also [integrate it to your IDE](https://docs.astral.sh/ruff/integrations/) to reformat
your code each time you save a file.

### Static analysis with `ruff`

To run static analysis, run `ruff` with:
```bash
ruff check src tests
```
or
```bash
make lint-check
```

To run static analysis and to apply auto-fixes, run `ruff` with:
```bash
make lint-fix
```
### Type checking with `mypy`

To type check your code, run `mypy` with:
```bash
mypy src --explicit-package-bases --namespace-packages
```
or
```bash
make type-check
```

## API

The project includes an API built with [FastAPI](https://fastapi.tiangolo.com/). Its code can be found at `src/api`.

The API is containerized using a [Docker](https://docs.docker.com/get-started/) image, built from the `Dockerfile` and `docker-compose.yml` at the root.

To build and start the API, use the following Makefile command:
```bash
make start-api
```
You can test the `hello_world` route by [importing the Postman collection](https://learning.postman.com/docs/getting-started/importing-and-exporting-data/#importing-postman-data) at `postman`.

For more details on the API routes, check the automatically generated [swagger](https://learning.postman.com/docs/getting-started/importing-and-exporting-data/#importing-postman-data) at the `/docs` url.

## Streamlit

The project includes a Streamlit app.
See its documentation in the [specific README](src/streamlit_app/README.md).
