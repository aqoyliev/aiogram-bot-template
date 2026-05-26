# aiogram-bot-template

A clean, batteries-included starter template for building Telegram bots with
[aiogram](https://docs.aiogram.dev/) 2.x. It gives you a sensible project
layout, throttling, an error handler, admin start-up notifications and bot
command registration out of the box, so you can focus on writing handlers.

> Use the green **"Use this template"** button on GitHub to spin up a new bot
> from this repository.

## Features

- 📁 Structured layout — handlers, keyboards, middlewares, states, filters and utils are pre-wired
- 🚦 Anti-flood throttling middleware
- 🛟 Centralized error handler for common Telegram API exceptions
- 🔔 Notifies admins when the bot starts
- 🧭 Registers default bot commands (`/start`, `/help`) automatically
- 🔐 Configuration via a `.env` file (`environs`)

## Requirements

- **Python 3.9** is recommended. aiogram 2.x pins `aiohttp 3.8.x`, which has no
  wheels for Python 3.11+ — installing on newer Python will fail to build.

## Quick start

```bash
# 1. Clone (or use "Use this template" on GitHub)
git clone https://github.com/aqoyliev/aiogram-bot-template.git
cd aiogram-bot-template

# 2. Create and activate a virtual environment (Python 3.9)
python3.9 -m venv .venv
source .venv/bin/activate          # Windows: .\.venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure your bot
cp .env.example .env               # Windows: Copy-Item .env.example .env
#    then edit .env and set BOT_TOKEN and ADMINS

# 5. Run
python app.py
```

## Configuration

Copy `.env.example` to `.env` and fill in your values:

| Variable    | Description                                              |
|-------------|----------------------------------------------------------|
| `BOT_TOKEN` | Token from [@BotFather](https://t.me/BotFather)          |
| `ADMINS`    | Comma-separated Telegram user IDs that count as admins   |
| `ip`        | Host IP address (used for deployment / webhooks)         |

`.env` is gitignored, so your secrets are never committed.

## Project structure

```
.
├── app.py                 # Entry point (long polling)
├── loader.py              # Bot & Dispatcher initialization
├── data/
│   └── config.py          # Reads settings from .env
├── handlers/
│   ├── users/             # start, help, echo handlers
│   ├── groups/            # group chat handlers
│   ├── channels/          # channel post handlers
│   └── errors/            # global error handler
├── keyboards/
│   ├── default/           # reply keyboards
│   └── inline/            # inline keyboards
├── middlewares/           # throttling middleware
├── states/                # FSM states
├── filters/               # custom filters
└── utils/
    ├── db_api/            # database helpers
    ├── misc/              # logging, throttling decorator
    ├── notify_admins.py   # start-up notification
    └── set_bot_commands.py
```

## License

[MIT](LICENSE) — based on
[anvarnarz/aiogram-bot-template](https://github.com/anvarnarz/aiogram-bot-template).
