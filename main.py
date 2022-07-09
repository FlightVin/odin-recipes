from flask import Flask, render_template

main = Flask(__name__)

@main.route('/')
def main_page():
    return render_template("index.html")

if (__name__ == "__main__"):
    main.run(debug=True)
