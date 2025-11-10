# src/tools/run_digest.py
import os
from github import Github
import requests

# Use GITHUB_TOKEN provided by Actions (or set a PAT in secrets for wider permissions)
G = Github(os.environ.get("GITHUB_TOKEN"))
REPO_NAME = os.environ.get("GITHUB_REPOSITORY", "landonattoian02-cmyk/student-life-dashboard")
REPO = G.get_repo(REPO_NAME)

def build_digest():
    try:
        task_label = REPO.get_label("task")
        issues = REPO.get_issues(labels=[task_label], state='open')
    except Exception:
        issues = REPO.get_issues(state='open')

    lines = []
    for i, issue in enumerate(issues):
        if i >= 10:
            break
        lines.append(f"- {issue.title} — {issue.html_url}")
    return "\n".join(lines) if lines else "No open tasks."

if __name__ == '__main__':
    digest = build_digest()
    webhook = os.environ.get('SLACK_WEBHOOK')
    if webhook:
        try:
            requests.post(webhook, json={"text": f"Daily Digest:\n{digest}"})
            print("Posted digest to Slack.")
        except Exception as e:
            print("Failed to post to Slack:", e)
            print("Digest content:\n", digest)
    else:
        print("Daily Digest:\n", digest)
