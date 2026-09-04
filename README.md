# Acme engineering interview

You will work on one of the questions in `questions/`. Your interviewer tells you which one at the start.

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env      # then paste the values your interviewer gives you
```

Python 3.11 or newer. Every question has a `starter.py` with the function signature we expect and a `README.md` with the task. Fixtures, when a question has them, live next to the starter.

## Using an AI model or coding agent

You may use any model or coding agent you like. Your interviewer gives you an OpenRouter key; put it in `.env` as `OPENROUTER_API_KEY`. The key is shared across candidates, so be reasonable with it.

Most tools only need two things: the key, and the base URL `https://openrouter.ai/api/v1`.

| Tool | How to point it at OpenRouter |
|---|---|
| Aider | reads `OPENROUTER_API_KEY`; run `aider --model openrouter/anthropic/claude-sonnet-4` |
| Cline | pick "OpenRouter" as the API provider and paste the key |
| OpenCode | set `OPENROUTER_API_KEY` and choose an `openrouter/...` model |
| Anything OpenAI-compatible | base URL `https://openrouter.ai/api/v1`, API key = the OpenRouter key |

Check your tool's own docs if it is not listed. Model ids are the ones from `https://openrouter.ai/api/v1/models`.

## What we look at

- The decisions, not the plumbing. Pagination and parsing are table stakes. What you count, what you refuse to guess, and what you label honestly is the interview.
- Whether you ran it. Print real output. Test the cases that worry you.
- Whether you can explain what your agent wrote.

State your assumptions in code comments or in the README of your question folder. Commit as you go if you like; we read the history too.

## Questions

| Folder | Task | Needs |
|---|---|---|
| `questions/ai_code_share` | Weekly AI-assisted share of a GitHub repository | GitHub API, a token from your interviewer |
| `questions/desktop_identity` | Attribute desktop usernames to employees and build the reporting tree | Fixtures in the folder, no network |
| `questions/flag_evaluator` | Evaluate feature flags and safely enable one for a single customer | Fixtures in the folder, no network |
| `questions/staged_rollout` | Plan a staged rollout from a public release catalog | GitHub Releases API, token optional |
| `questions/ai_spend` | Monthly AI spend by person and team, reconciled to the vendor | OpenRouter API with your key |
