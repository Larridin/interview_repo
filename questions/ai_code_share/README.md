# AI Code Share

Acme wants to know what fraction of a repository's work is AI-assisted, week by week. The only signal available today is git itself: AI coding tools add a trailer such as `Co-Authored-By: Copilot <...>` to the commits they helped write.

Write a function that, for a GitHub repository and the last N weeks, returns weekly totals of commits, AI-assisted commits and the share, plus a per-author breakdown. Which co-author identities count as AI is configuration, not a hardcoded list: the caller passes `ai_identities`.

## APIs

- List commits: `GET https://api.github.com/repos/{owner}/{repo}/commits` with `since`, `until`, `per_page`. Paginated through the `Link` response header. Docs: https://docs.github.com/en/rest/commits/commits
- Single commit (adds `stats` and `files`): `GET .../commits/{sha}`
- Auth: `Authorization: Bearer <token>`. Your interviewer will share a token; put it in `.env` as `GITHUB_TOKEN`. Rate limits: https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api

Decide and state: what counts as a commit (merge commits? bot authors?), how weeks are bucketed, and what happens to a co-author trailer that matches no identity.

## Starter

`starter.py` has the signature and the return shape. Run it with:

```bash
python starter.py github github-mcp-server 8
```

## Follow-ups

- Testing: how would you test this without calling GitHub? What do your fixtures look like?
- Performance: a line-level share needs one request per commit. Make it fast. What is safe to cache forever?
- Architecture: add GitLab as a second provider. GitLab squash merges rewrite the commit message. What does your metric say about that repository?
- Product: a developer uses an AI tool that never writes trailers. Your dashboard says 0% for them. What do you show, and how do you label it honestly?
- Product: 30% of the commits have two parents. Is that work?
