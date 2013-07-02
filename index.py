from flask import Flask, render_template
from forms import InformationForm

app = Flask(__name__)
app.secret_key= 'experiment@2013'

@app.route('/training')
def training():
    """


    :return:
    """
    return "Training"

@app.route('/')
def home():
    form=InformationForm()
    return render_template('home.html',form=form)

@app.route('/testing')
def testing():
  return render_template('testing.html')


if __name__ == '__main__':
    app.run(debug=True)