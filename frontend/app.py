from flask import Flask, render_template
import search 

app = Flask(__name__)

@app.route("/")
def main_page():
    results = ["falan", "filan", "ortam"]

    return render_template('main.html', results=results)


if __name__ == "__main__":
    app.debug = True
    app.run()
