# Contributing to bgg-pi

First off, thanks for taking the time to contribute! 🎉

## How to Contribute

1.  **Fork the repository** on GitHub.
2.  **Clone your fork** locally.
    ```bash
    git clone https://github.com/your-username/bgg-pi.git
    cd bgg-pi
    ```
3.  **Create a virtual environment** and install dependencies.
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -e .
    pip install pytest pytest-asyncio ruff
    ```
4.  **Create a branch** for your changes.
    ```bash
    git checkout -b feature/amazing-feature
    ```
5.  **Make your changes** and run tests.
    ```bash
    pytest tests/
    ```
6.  **Lint your code** using Ruff.
    ```bash
    ruff check src/ tests/
    ruff format src/ tests/
    ```
7.  **Commit your changes** and push to your fork.
8.  **Submit a Pull Request**!

## Development Standards

*   **Async First**: All I/O bound operations must be asynchronous (using `aiohttp`).
*   **Type Hinting**: All code must be fully type-hinted.
*   **Testing**: New features must include tests. We aim for high test coverage.
*   **Code Style**: We use `ruff` for linting and formatting.
