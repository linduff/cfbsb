from flask import Flask, render_template
import os
from dotenv import load_dotenv
import cfbd

load_dotenv()
configuration = cfbd.Configuration(
    access_token = os.environ["API_TOKEN"]
)

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("scoreboard.html")



if __name__ == "__main__":
    app.run()