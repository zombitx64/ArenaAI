# ArenaAI Poker Tournament

This repository hosts a simple AI-vs-AI poker tournament with a leaderboard and
basic websocket broadcasting of game events.

## Running

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the tournament and broadcaster (plays 20 rounds by default):

```bash
python main.py
```

You can customize the number of rounds by importing `run_tournament` and
passing a value:

```bash
python - <<'PY'
from main import run_tournament
run_tournament(5)
PY
```

A websocket server will be available on `ws://localhost:8765` streaming round
updates and leaderboard standings.

## Testing

```bash
python -m pytest
```
