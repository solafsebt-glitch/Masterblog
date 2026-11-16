from flask import Flask,render_template
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
@app.route('/')
def index():
    # add code here to fetch the job posts from a file
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)