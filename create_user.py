from werkzeug.security import generate_password_hash
from db import db, cursor

username = "username"
password = "eivinderbest"

hashed_password = generate_password_hash(password)

cursor.execute(
    "INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)",
    (username, hashed_password, "admin")
)




db.commit()

print("Bruker er opprettet")