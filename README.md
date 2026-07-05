# pf-agent

> An autonomous AI code-review agent — point it at a codebase and get back structured,
> actionable findings with suggested fixes.

**Status:** 🚧 early development. The CLI skeleton and project tooling are in place; the
review engine is being built incrementally (see the [Roadmap](#roadmap)).

## Overview

`pf-agent` reads a repository (or a single file), builds a searchable understanding of the
code, runs an LLM agent loop to find issues, and outputs a structured review with suggested
fixes. It's designed around a pluggable LLM provider layer so it can run against a local
model (Ollama) or a hosted API (OpenAI / Anthropic).

## Quickstart

Requires [uv](https://docs.astral.sh/uv/) and Python 3.12+.

```bash
# clone, then from the project root:
uv sync                          # create the environment from the lockfile
uv run pf-agent review ./src     # review a path
```

## Usage

```bash
uv run pf-agent --help           # list commands
uv run pf-agent review <path>    # review the given file or folder
```

## Tech stack

- **Python 3.12**, packaged with **uv** (`src` layout, hatchling build backend)
- **Typer** — CLI
- **ruff** (lint + format) and **pytest** (tests)

## Roadmap

- [x] Project scaffolding, packaging, and a validated CLI skeleton
- [ ] **v0** — structured findings (`Finding` schema), an LLM provider abstraction, and a
      single-shot review that prints findings as a table
- [ ] **v1** — RAG over a repo: AST-aware chunking (tree-sitter), embeddings + a vector DB,
      and context retrieval before review
- [ ] **v2** — an agentic loop (retrieve → analyze → self-critique → fix), unified-diff
      output, and a FastAPI service with streaming progress
- [ ] **v3** — an evaluation harness (precision/recall on known-buggy fixtures) and PR-diff
      review

## Development

```bash
uv run ruff check      # lint
uv run ruff format     # format
uv run pytest          # tests
```
