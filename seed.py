import faker
import sqlite3
import random
from random import choice, randint


def generate_fake_data():
    fake_fullnames = []
    fake_emails = []
    fake_names = ['new', 'in progress', 'completed']
    fake_titles = []
    fake_descriptions = []
    
    fake_data = faker.Faker()

    for _ in range(30):
        fake_fullnames.append(fake_data.name())
        fake_emails.append(fake_data.email())
        fake_titles.append(fake_data.sentence())
        fake_descriptions.append(fake_data.paragraph())

    return fake_fullnames, fake_emails, fake_names, fake_titles, fake_descriptions



def prepare_data(fullnames, emails, names, titles, descriptions):
    for_users = []
    for email in emails:
        for_users.append((choice(fullnames), email))
    
    for_status = [(status, ) for status in names]

    for_tasks = []
    for task in titles:
        for_tasks.append((task, choice(descriptions), randint(1, 3), randint(1, 30)))


    return for_users, for_status, for_tasks

def insert_data_to_db(users, status, tasks):

    with sqlite3.connect('data.db') as con:
        cur = con.cursor()

    sql_to_users = """INSERT INTO users(full_name, email)
                       VALUES (?, ?)"""
    cur.executemany(sql_to_users, users)

    sql_to_status = """INSERT INTO status(name)
                       VALUES (?)"""
    cur.executemany(sql_to_status, status)

    sql_to_tasks = """INSERT INTO tasks(title, description, status_id, user_id)
                       VALUES (?, ?, ?, ?)"""
    cur.executemany(sql_to_tasks, tasks)

    con.commit()


if __name__ == "__main__":
    fullnames, status, tasks = prepare_data(*generate_fake_data())
    insert_data_to_db(fullnames, status, tasks)
