from flask import Flask, jsonify, abort, request
app = Flask(__name__)

posts = [
    {
        'id': 1,
        'title': 'FlaskTutorial1',
        'Description': 'HelloWorld Program',
        'author': 'narendravardi'
    },
    {
        'id': 2,
        'title': 'FlaskTutorial2',
        'Description': 'Flask Views Program',
        'author': 'narendravardi'
    }
]

@app.route('/blogpost/api/blogs', methods = ['GET'])
def list_blogs():
    return jsonify(posts)

@app.route('/blogpost/api/blog/<int:id>')
def get_blog_by_id(id):
    for blog in posts:
        if blog['id'] == id:
            return jsonify(blog)
    return abort(404)

@app.route('/blogpost/api/blog/create', methods = ['POST'])
def create_blog_post():
    new_id = len(posts)
    if 'title' not in request.json:
        abort(400)
    new_post = {
        'id' : new_id + 1,
        'title': request.json.get('title'),
        'description': request.json['description'],
        'author': request.json['author']
    }
    posts.append(new_post)
    return jsonify(posts)



if __name__ == '__main__':
	app.run(debug=True)