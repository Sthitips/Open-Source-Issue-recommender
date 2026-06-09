import requests

repos=["facebook/react",
       "microsoft/vscode",
       "tensorflow/tensorflow",
       "langchain-ai/langchain",
       "pallets/flask"]

data=[]

for repo in repos:
    print(f"Fetching {repo}")
    repo_url= f"https://api.github.com/repos/{repo}/issues"
    response= requests.get(repo_url)
    issues= response.json()
    for issue in issues:
        if "pull_request" in issue:
            continue
        title=issue["title"]
        body=issue["body"]
        url=issue["html_url"]
        labels=[label["name"] for label in issue["labels"]]
        labels_text=" ".join(labels)
        data.append({
            "repo":repo,
            "title": title,
            "body": body,
            "labels": labels_text,
            "url": url
        })

import pandas as pd

df=pd.DataFrame(data)
df.to_csv("og_issues.csv", index=False)
print(df.shape)
