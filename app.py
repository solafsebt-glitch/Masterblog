from flask import Flask,render_template,request, redirect, url_for
import json
import os

app = Flask(__name__)

# Function to load posts from the JSON file
def load_posts():
    file_path = 'posts.json'
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# Function to save posts to the JSON file
def save_posts(posts):
    file_path = 'posts.json'
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=4, ensure_ascii=False)

@app.route('/')
def index():
    # add code here to fetch the job posts from a file
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)


# Add Route (/add)
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        blog_posts = load_posts()

        # Get data from form
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')

        # Generate a unique ID for the new post
        new_id = max([p['id'] for p in blog_posts], default=0) + 1

        # Create new post dictionary
        new_post = {
            "id": new_id,
            "title": title,
            "author": author,
            "content": content
        }

        # Append and save to JSON file
        blog_posts.append(new_post)
        save_posts(blog_posts)

        # Redirect back to home page
        return redirect(url_for('index'))

    return render_template('add.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)