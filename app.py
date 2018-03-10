from flask import Flask, url_for, request, g
import sqlite3
from posts import posts
app = Flask(__name__)
app.database = 'flask.db'

posts = {}

@app.route('/')
def home():
    return 'The following are the list of commands supported: 1. Create \n 2. List \n 3. Edit \n 4. Delete \n 5. Get'


@app.route('/create')
def create():
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    posts_info = []
    for row in cur.fetchall():
        posts_obj = posts
        posts_info.append(row)
    g.db.close()
    return str(posts_info)

@app.route('/list')
def list():
    return 'Please find the list of blog posts available!'

@app.route('/edit')
def edit():
    return 'Your edit is updated!'

@app.route('/delete')
def delete():
    return 'your post is successfully deleted!'

@app.route('/get/<int:id>')
def get_post_by_id(id):
    return "Here's the blog post with id: {} ".format(id)


def connect_db():
    return sqlite3.connect(app.database)


if __name__ == '__main__':
	app.run(debug=True)