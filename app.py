from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def index():
    f = open('data.json')
    blog_posts = json.load(f)
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run()