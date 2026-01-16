# 🎲 bgg-pi

[![PyPI version](https://img.shields.io/pypi/v/bgg-pi?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/bgg-pi/)
[![Python Versions](https://img.shields.io/pypi/pyversions/bgg-pi?style=for-the-badge&logo=python&logoColor=white)](https://pypi.org/project/bgg-pi/)
[![Tests](https://img.shields.io/github/actions/workflow/status/seanmccabe/bgg-pi/tests.yaml?branch=main&style=for-the-badge&logo=github)](https://github.com/seanmccabe/bgg-pi/actions)
[![Code Style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&style=for-the-badge)](https://github.com/astral-sh/ruff)
[![License](https://img.shields.io/github/license/seanmccabe/bgg-pi?style=for-the-badge)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)

**A modern, high-performance asynchronous Python client for BoardGameGeek.**

`bgg-pi` is designed for developers who need reliable, non-blocking access to BoardGameGeek data. Whether you're building a Home Assistant integration, a discord bot, or a data analysis tool, `bgg-pi` makes it effortless.

## ✨ Features

*   🚀 **Fully Async**: Built on top of `aiohttp` to keep your applications responsive.
*   ✍️ **Record Plays**: One of the few libraries that supports **logging plays** directly to a BGG account.
*   📦 **Collection Management**: Fetch user collections with options to filter by ownership, wishlist status, and more.
*   🎨 **Rich Metadata**: Retrieve high-fidelity game details including box art, ranks, weight, and play times.
*   🛡️ **Type Safe**: Fully typed codebase for excellent IDE autocompletion and error checking.

## 🚀 Installation

Install via pip:

```bash
pip install bgg-pi
```

## 🛠️ Quick Start

### Fetching User Plays

```python
import asyncio
import aiohttp
from bgg_pi import BggClient

async def main():
    async with aiohttp.ClientSession() as session:
        client = BggClient(session, username="your_username")
        
        # specific api token is optional for public data but recommended
        plays = await client.fetch_plays()
        
        print(f"Found {plays['total']} plays!")
        # Access simple play data
        if plays['last_play']:
             print(f"Last played: {plays['last_play']['game']} on {plays['last_play']['date']}")

if __name__ == "__main__":
    asyncio.run(main())
```

### Logging a Play

Authenticate securely and log your gaming sessions:

```python
async def log_play():
    async with aiohttp.ClientSession() as session:
        # Password is required for play logging
        client = BggClient(session, username="seanmccabe", password="secret_password")
        
        if await client.login():
            success = await client.record_play(
                game_id=13,  # Catan
                date="2026-01-16",
                comments="Great game with friends!",
                length="90",
                players=[
                    {"name": "Sean", "win": True, "score": "10"},
                    {"name": "Friend", "win": False, "score": "8"}
                ]
            )
            
            if success:
                print("Play recorded successfully!")
```

## 📚 Documentation

The client covers the most essential BGG XML API2 and GeekPlay endpoints:

*   `fetch_plays()`: Get logged plays.
*   `fetch_collection()`: Get a user's board game collection (with filters).
*   `fetch_thing_details([ids])`: Get detailed metadata for specific games.
*   `fetch_game_plays(id)`: Get play counts for a specific game.
*   `record_play(...)`: Post a new play to BGG.

## 📦 Projects using `bgg-pi`

*   [**Home Assistant BoardGameGeek Integration**](https://github.com/seanmccabe/bgg-sync): A comprehensive integration for tracking collection and plays in Home Assistant.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1.  Fork the repository
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
