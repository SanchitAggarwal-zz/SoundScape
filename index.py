from flask import Flask, render_template, request, flash
from forms import InformationForm

app = Flask(__name__)
app.secret_key = 'experiment@2013'

@app.route('/',methods=['GET','POST'])
def home():
    form=InformationForm()
    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required.')
            return render_template('home.html', form=form)
        else:
            return 'Form Posted.'
    elif request.method == 'GET':
        return render_template('home.html',form=form)

@app.route('/training')
def training():

     return render_template('training.html')

@app.route('/testing')
def testing():
  return render_template('testing.html')


if __name__ == '__main__':
    app.run(debug=True)