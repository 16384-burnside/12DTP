from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html', title='About')

@app.route('/search')
def search():
    conn = sqlite3.connect('calisthenics.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Exercise;")
    results = cur.fetchall()
    return render_template("search.html", page_title="Search", results=results)

if __name__ == '__main__':
  app.run(debug=True)
