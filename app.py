from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    original = ""
    reversed_string = ""

    if request.method == 'POST':
        original = request.form['text']
        reversed_string = original[::-1]

    return render_template(
        'index.html',
        original=original,
        reversed_string=reversed_string
    )

if __name__ == '__main__':
    app.run(debug=True)
