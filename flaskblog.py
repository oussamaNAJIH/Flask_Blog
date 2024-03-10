from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        "author": "John Doe",
        "title": "First Post",
        "content": "This is the content of the first post.",
        "date_posted": "2024-03-10"
    },
    {
        "author": "Jane Smith",
        "title": "Second Post",
        "content": "This is the content of the second post.",
        "date_posted": "2024-03-11"
    },
    {
        "author": "Alice Johnson",
        "title": "Third Post",
        "content": "This is the content of the third post.",
        "date_posted": "2024-03-12"
    }
]


@app.route("/")
@app.route("/home")
def hello_world():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="about")


if __name__ == "__main__":
    app.run(debug=True)