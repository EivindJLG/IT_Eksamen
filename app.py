from flask import Flask, render_template, request, redirect
from werkzeug.security import check_password_hash
from db import db, cursor

app = Flask(__name__)

@app.route("/")
def home():
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        cursor.execute(
            "SELECT * FROM users WHERE username = %s",
            (username,)
        )

        user = cursor.fetchone()

        if user and check_password_hash(user["password_hash"], password):

            cursor.execute(
                """
                INSERT INTO logs
                (event_type, message, severity)
                VALUES (%s, %s, %s)
                """,
                (
                    "LOGIN_SUCCESS",
                    f"Bruker {username} logget inn",
                    "INFO"
                )
            )

            db.commit()

            return redirect("/dashboard")

        cursor.execute(
            """
            INSERT INTO logs
            (event_type, message, severity)
            VALUES (%s, %s, %s)
            """,
            (
                "LOGIN_FAIL",
                f"Feil brukernavn eller passord for {username}",
                "WARNING"
            )
        )

        db.commit()

        return "Feil brukernavn eller passord"
        return render_template("login.html")
    
@app.route("/dashboard")
def dashboard():

    cursor.execute(
        """
        SELECT * 
        FROM logs
        ORDER BY timestamp DESC
        """
    )

    logs = cursor.fetchall()

    return render_template("dashboard.html", logs=logs)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")