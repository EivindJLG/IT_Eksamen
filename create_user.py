from werkzeug.security import generate_password_hash
from db import db, cursor
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("ADMIN_USER")
password = os.getenv("ADMIN_PASSORD")

hashed_password = generate_password_hash(password)

cursor.execute(
    "INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)",
    (username, hashed_password, "admin")
)




db.commit()

print("Bruker er opprettet")