import json
import random
from datetime import datetime, timedelta

users = ["user1", "user2", "user3"]
tags = ["shop", "work", "income", "trip", "charity", "freelance"]

transactions = []

for _ in range(300):
    transaction = {
        "user": random.choice(users),
        "date": (datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d'),
        "amount": round(random.uniform(10, 1000), 2),
        "currency": random.choice(['$', '€']),
        "in_out": random.choice(['in', 'out']),
        "tag": random.choice(tags)
    }
    transactions.append(transaction)

with open('transactions.json', 'w') as file:
    json.dump(transactions, file, indent=4)
