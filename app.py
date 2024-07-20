from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        with open('database.json','r', encoding="utf-8") as f:
            blog_posts = json.load(f)
        return render_template('index.html', posts=blog_posts)
    
    if request.method == 'POST':
        with open('database.json','r', encoding="utf-8") as f:
            blog_posts = json.load(f)
        post_id = int(request.form.get('post_id'))
        return render_template('delete.html', posts=blog_posts, post_id=post_id)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        new_post = {"author": author, "title": title, "content": content}

        with open('database.json','r', encoding="utf-8") as f:
            blog_posts = json.load(f)

        if blog_posts:
            latest_id = max(post['id'] for post in blog_posts)
        else:
            latest_id = 0

        new_post["id"] = latest_id + 1
        blog_posts.append(new_post)

        with open('database.json','w', encoding="utf-8") as f:
            json.dump(blog_posts, f, indent=4)

        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete/<int:post_id>', methods=['GET', 'POST'])
def delete(post_id: int):
    if request.method == 'GET':
        with open('database.json') as f:
            blog_posts = json.load(f)
        return render_template('delete.html', posts=blog_posts, post_id=post_id)
    
    if request.method == 'POST':
        with open('database.json') as f:
            blog_posts = json.load(f)

        blog_posts = [post for post in blog_posts if post['id'] != post_id]

        with open('database.json', 'w') as f:
            json.dump(blog_posts, f, indent=4)
        
        return redirect(url_for('index'))
    

# @app.route('/update/<int:post_id>', methods=['GET', 'POST'])
# def update(post_id):
#     # Fetch the blog posts from the JSON file
#     post = fetch_post_by_id(post_id)
#     if post is None:
#         # Post not found
#         return "Post not found", 404
    
#     if request.method == 'POST':
#         # Update the post in the JSON file
#         # Redirect back to index

#     # Else, it's a GET request
#     # So display the update.html page
#     return render_template('update.html', post=post)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4999)