# src/app.py
from fastapi import FastAPI, Request
import os
from tasks.slack_handler import enqueue_slack_event
from tasks.gmail_handler import enqueue_gmail_event

app = FastAPI()

@app.get("/health")
async def health():
return {"status": "ok"}

@app.post("/slack/events")
async def slack_events(req: Request):
payload = await req.json()
# handle url_verification if present
if payload.get("type") == "url_verification":
return {"challenge": payload.get("challenge")}
event = payload.get("event", {})
# enqueue worker task
enqueue_slack_event(event)
return {"ok": True}

@app.post("/gmail/push")
async def gmail_push(req: Request):
payload = await req.json()
# Gmail push notifications are minimal; you must fetch the message using Gmail API
enqueue_gmail_event(payload)
return {"ok": True}
