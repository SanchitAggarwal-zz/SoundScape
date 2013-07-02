#Creating python form for information about the Tester
from flask.ext.wtf import Form, TextField, RadioField, IntegerField, SelectField, SubmitField,validators, ValidationError

class InformationForm(Form):
    firstname = TextField("FirstName")
    lastname = TextField("LastName")
    gender = RadioField("Gender", choices = ['Male', 'Female'])
    age = IntegerField("Age")
    blindtype = SelectField("BlindType",choices=['Congential','Accidental','Non-Blind'])
    email = TextField("Email")
    contact = IntegerField("Contact")
    submit = SubmitField("Send")