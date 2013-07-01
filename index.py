from flask import Flask, render_template

app = Flask(__name__)


@app.route('/training')
def training():
    return "Training"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/testing')
def testing():
  return render_template('testing.html')


if __name__ == '__main__':
    app.run(debug=True)