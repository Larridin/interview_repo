# AI spend by person and team

Acme pays for three AI tools and has no idea what they cost per team. You have each vendor's usage export, HR's roster, a public price list, and the gateway's own per-request accounting. Produce a monthly spend report that a finance person will trust: every dollar lands in exactly one bucket, the buckets sum to the total, and where the vendor kept its own books your number is checked against theirs.

## Inputs

- `data/usage.jsonl`, one row per line.
  - Token-billed rows: `{"ts", "tool", "user_email", "model", "input_tokens", "output_tokens", "cached_input_tokens", "generation_id"}`. These went through Acme's OpenRouter gateway, and `generation_id` is the gateway's id for the request.
  - Cursor rows: `{"ts", "tool": "cursor", "user_email", "spend_cents"}`
  - Copilot rows: `{"ts", "tool": "copilot", "user_email", "event": "active"}`
  - `user_email` may be null.
- `data/employees.csv`: `email, display_name, manager_email, department, deleted_at`
- `tools.yaml`: how each tool is billed and how vendor model ids map to the price list.
- Prices: `GET https://openrouter.ai/api/v1/models`. Docs: https://openrouter.ai/docs/api-reference/list-available-models. Prices are USD per token.
- Vendor accounting: `GET https://openrouter.ai/api/v1/generation?id={generation_id}` with the key you were given (`OPENROUTER_API_KEY` in `.env`) returns what the gateway actually charged: `total_cost`, native token counts and `provider_name`. Docs: https://openrouter.ai/docs/api-reference/get-a-generation

`starter.py` has the report shape. Run it with `python starter.py 2026-08`.

## Follow-ups

- A model in the export has no entry in the price list. What does the report show for it?
- The vendor changed a price on the 12th. Where does that live, and what happens to the first eleven days?
- Every vendor restates the trailing 30 days. Finance already sent last month's number to the board. Is your pipeline idempotent, and does it remember what it said before?
- Only 4 of 21 Copilot seats had any activity. What is the cost per active seat, and is that the right number to show?
- Your computed cost and the vendor's `total_cost` disagree by a few percent on one model. List the reasons that could be true before you call it a bug.
- `provider_name` says Amazon Bedrock for requests you priced as Anthropic. Does finance care? Does security?
- Some engineers use the same models through a cloud provider that appears in none of these exports. Does your report call them non-users?
