from flask import Flask, render_template, request, g, Response
import sqlite3
import time

app = Flask(__name__)
app.database = 'blogposts.db'

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/create', methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('Blog.html')
    elif request.method == 'POST':
        form_data = request.form
        author = form_data['author']
        title = form_data['title']
        description = form_data['description']
        id = int(time.time())
        g.db = connect_db()
        g.db.execute(get_insert_query(id, author, title, description))
        g.db.commit()
        g.db.close()
        return 'Successfully created the blog with id: {}'.format(id)
    else:
        return 'Not a valid HTTP method for this API endpoint!'


@app.route('/list')
def list():
    g.db = connect_db()
    cur = g.db.execute('select * from posts')

    all_posts = []

    for row in cur.fetchall():
        single_post = {}
        single_post['id']= row[0]
        single_post['author']= row[1]
        single_post['title']= row[2]
        single_post['description']= row[3]
        all_posts.append(single_post)

    return Response(str(all_posts),  content_type='application/json; charset=utf-8')

@app.route('/delete/<string:id>', methods = ['DELETE'])
def delete(id):
    g.db = connect_db()
    g.db.execute("delete from posts where id = '{}' ".format(id))
    g.db.commit()
    g.db.close()
    return 'successfully deleted post with id: {}'.format(id)


@app.route('/edit/<string:id>', methods = ['PUT'])
def edit(id):
    g.db = connect_db()
    form_data = request.form
    description = form_data['description']
    g.db.execute("UPDATE POSTS SET description = '{}' WHERE ID = {}".format(description, id))
    g.db.commit()
    g.db.close()
    return 'updated the post with id: {}'.format(id)



def connect_db():
    return sqlite3.connect(app.database)

def get_insert_query(id, author, title, description):
    return "insert into posts values('{}', '{}', '{}', '{}')".format(id, author, title, description)

if __name__ == '__main__':
	app.run(debug=True)