from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    with open('database.json') as f:
        blog_posts = json.load(f)
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        new_post = {"author": author, "title": title, "content": content}

        with open('database.json') as f:
            blog_posts = json.load(f)

        if blog_posts:
            latest_id = max(post['id'] for post in blog_posts)
        else:
            latest_id = 0

        new_post["id"] = id + 1
        blog_posts.append(new_post)

        with open('database.json') as f:
            f.dump(blog_posts, f, indent=4)

        return redirect(url_for('index.html'))

    return render_template('add.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4999)