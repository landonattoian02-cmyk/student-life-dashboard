# src/tasks/slack_handler.py
from redis import Redis
from rq import Queue

redis_conn = Redis.from_url("${REDIS_URL}")
q = Queue("default", connection=redis_conn)

def enqueue_slack_event(event):
q.enqueue(handle_slack_event, event)

def handle_slack_event(event):
# minimal parser: look for scheduling keywords
text = event.get("text", "")
user = event.get("user")
# TODO: call agent to decide action
print("Received slack event:", text)
