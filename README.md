# student-life-dashboard

AI-powered school, college app, and mock trial organizer — student-focused starter scaffold.

## Goals
- Turn emails/messages into tracked tasks (GitHub Issues)
- Auto-draft replies and save attachments to Google Drive
- Create calendar events for deadlines
- Post daily/weekly digests

## Quickstart (prototype)
1. Create this repo on GitHub (you already did).
2. Add the files from this scaffold to the repo.
3. Create GitHub Actions secrets (see `infra/SECRETS.md`).
4. Deploy the FastAPI app to Cloud Run / Fly / Heroku, or run locally with Docker.

## Files in this scaffold
- `.github/workflows/daily_digest.yml` — scheduled digest job
- `.github/ISSUE_TEMPLATE/task.md` — issue template for tasks
- `src/app.py` — FastAPI webhook endpoints
- `src/tasks/` — handler stubs (gmail_handler.py, slack_handler.py, agent.py)
- `Dockerfile`, `requirements.txt`

## Next steps I can do for you
- Generate a full GitHub Actions CI + deploy workflow
- Create Zapier/Make templates to connect Gmail & Slack to this repo
- Help you configure Google OAuth and Slack app

---
