import requests

url = "https://jira.dep.local/rest/api/2/issue/DO-2533/notify"

notify_data = {
        "subject": "Issues with the ticket",
        "textBody": "Check the issue and resolve.",
        "htmlBody": "bug raised <strong>html<strong>",
        "to": {
            "users": ["malasri@gmail.com"]
        },

    }

a=requests.post(url,auth=('malasri.c','Malasreech@1997'), json=notify_data)
print(a.text)
