class posts(object):
    def __init__(self, id, title, body, author):
        self.id = id
        self.title = title
        self.body = body
        self.author = author

    def post_from_form(self, request_form):
        id = request_form['id']
        title = request_form['title']
        body = request_form['body']
        author = request_form['author']
        return posts(id, title, body, author)