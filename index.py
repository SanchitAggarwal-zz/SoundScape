from flask import Flask, render_template, request, flash
from forms import InformationForm,TestForm,TrainingForm
import csv
import synthesis
#import xlwt

app = Flask(__name__)
app.secret_key = 'experiment@2013'
CSRF_ENABLED = True
Information = False
row=[]

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
            row.append(form.firstname.data)
            row.append(form.lastname.data)
            row.append(form.age.data)
            row.append(form.gender.data)
            row.append(form.blindtype.data)
            row.append(form.email.data)
            row.append(form.contact.data)
            #save(row)#.gender.choices[form.gender.data])
            global Information
            Information= True
            trainingform=TrainingForm()
            #synthesis.Experiment(1,1,1,0,1)
            return render_template('training.html',form=trainingform)
        else:
            print form.errors
            flash('All fields are required.')
            return render_template('home.html', form=form)
    elif request.method == 'GET':
        return render_template('home.html',form=form)

@app.route('/training',methods=['GET','POST'])
def training():
    #synthesis.Experiment(-5,1,1,0,1)
    #return render_template('training.html')
    global Information
    if Information:
        trainingform=TrainingForm()
        if request.method == 'POST':
            testform=TestForm()
            return render_template('testing.html',form=testform)
        else:
            return render_template('training.html',form=trainingform)
    else:
        form=InformationForm()
        return render_template('home.html',form=form)

@app.route('/testing',methods=['GET','POST'])
def testing():
    testform=TestForm()
    global Information
    if Information:
        if request.method == 'POST':
            print "saving"
            row.append(testform.correct.data)
            row.append(testform.wrong.data)
            row.append(testform.attempt.data)
            save(row)
            del row[:]
            Information=False
            form=InformationForm()
            return render_template('home.html',form=form)
        return render_template('testing.html',form=testform)
    else:
        form=InformationForm()
        return render_template('home.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)