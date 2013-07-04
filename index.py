from flask import Flask, render_template, request, flash
from forms import InformationForm
import csv
import synthesis
#import xlwt


app = Flask(__name__)
app.secret_key = 'experiment@2013'
CSRF_ENABLED = True
#Information = False

def save(row):
    csvfile=open("Experiment.xls","a")
    writer = csv.writer(csvfile)
    writer.writerow(row)

    '''workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('UserInfo')
    for i in range(0,len(row)):
        worksheet.write(0,i,row[i])
    workbook.save('Experiment2.xls')'''

@app.route('/',methods=['GET','POST'])
def home():
    form=InformationForm()
    if request.method == 'POST':
        if form.validate():
            row=[]
            row.append(form.firstname.data)
            row.append(form.lastname.data)
            row.append(form.age.data)
            row.append(form.gender.data)
            row.append(form.blindtype.data)
            row.append(form.email.data)
            row.append(form.contact.data)
            save(row)#.gender.choices[form.gender.data])
            #Information=True
            synthesis.Experiment(1,1,1,0,1)
            return render_template('training.html')
        else:
            print form.errors
            flash('All fields are required.')
            return render_template('home.html', form=form)
    elif request.method == 'GET':
        return render_template('home.html',form=form)

@app.route('/training')
def training():
    #synthesis.Experiment(-5,1,1,0,1)
    return render_template('training.html')
    '''if Information:
        print Information
        return render_template('training.html')
    else:
        print Information
        form=InformationForm()
        return render_template('home.html',form=form)'''

@app.route('/testing')
def testing():
  return render_template('testing.html')


if __name__ == '__main__':
    app.run(debug=True)