import subprocess


def new_db():
    subprocess.run(['python', 'database/kill_db.py'])
    subprocess.run(['python', 'database/init_db.py'])
