# Python Scripts Challenges

This project is a Python 3.12 workspace managed with `uv`.

It contains standalone Python practice scripts and is also ready to grow into a
FastAPI backend.

## Requirements

- Python 3.12
- `uv`

The project pins Python with `.python-version`:

```txt
3.12
```

Install/sync the local environment:

```bash
uv sync
```

Check the Python version used by `uv`:

```bash
uv run python --version
```

## Run Python Scripts Locally

Run scripts from the project root with:

```bash
uv run python path/to/script.py
```

Examples:

```bash
uv run python py_scripts_codewars/anagram.py
uv run python py_scripts_codewars/supermarket_queue.py
uv run python scripts_genepy.org/basics.py
uv run python scripts_chatgpt/list_comprehension_map_filter_reduce_lvl1.py
```

Using `uv run python ...` makes sure the script runs with the project Python
version and environment, instead of a random global Python installation.

## Project Folders

- `py_scripts_codewars/`: Codewars practice challenges.
- `scripts_genepy.org/`: Genepy.org practice scripts.
- `scripts_chatgpt/`: Extra Python practice scripts.
- `main.py`: FastAPI app entry point, in case of backend purposes.

## Run The FastAPI App Locally

The project already includes a minimal FastAPI app in `main.py`.

Start the development server:

```bash
uv run fastapi dev
```

Then open:

```txt
http://127.0.0.1:8000
```

API docs are available at:

```txt
http://127.0.0.1:8000/docs
```

If automatic discovery ever fails, run it explicitly:

```bash
uv run fastapi dev main.py
```

## Dependency Notes

Runtime dependencies are in `[project.dependencies]`.

Development-only dependencies are in `[dependency-groups].dev`.

For local development, use:

```bash
uv sync
```

For a production-style install without dev dependencies, use:

```bash
uv sync --no-dev
```
