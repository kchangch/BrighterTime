import requests
import csv

response = requests.get(
    "https://no1u9vwrh1.execute-api.us-east-2.amazonaws.com/prod")

content = response.json()
content = content['body']['data']

fieldnames = ['userEmail', 'challengesCompleted']

with open("ranking.csv", "w", encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(content)
