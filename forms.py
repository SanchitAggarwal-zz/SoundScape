#Creating python form for information about the Tester
from flask.ext.wtf import Form, TextField, RadioField, IntegerField, SelectField, SubmitField,validators, ValidationError

class InformationForm(Form):
    firstname = TextField("First Name",[validators.Required("First Name Required")])
    lastname = TextField("Last Name",[validators.Required("Last Name Required")])
    age = IntegerField("Age",[validators.Required("Age Required")])
    email = TextField("Email",[validators.Required("Email Required"),validators.Email("abc@company.com")])
    contact = IntegerField("Contact",[validators.Required("Contact Required")])
    gender = SelectField(u'Gender', choices = [('Male','Male'),('Female','Female')])
    blindtype = SelectField(u'Blind Type',choices=[('Congential','Congential'),('Accidental','Accidental'),('Non-Blind','Non-Blind')])
    submit = SubmitField("Send")