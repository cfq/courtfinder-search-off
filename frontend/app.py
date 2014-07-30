from flask import Flask, render_template, url_for, request
from search import search_keyword 

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('main.html', results=[])


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
    else:
        query = request.args.get('query')

    res = search_keyword( query )

    return render_template('main.html', results=res['hits'], query=query)


if __name__ == "__main__":
    app.debug = True
    app.run()
