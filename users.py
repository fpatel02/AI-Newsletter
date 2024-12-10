# users.py

import csv

# Load users from csv
def load_users(file = 'users.csv'):
    users = []
    with open(file, mode = 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            users.append(row[0]) 
    return users

# Add a new user
def add_user(email, file = 'subscribers.csv'):
    with open(file, mode = 'a', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow([email])