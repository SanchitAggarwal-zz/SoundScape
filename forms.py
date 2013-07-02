#Creating python form for information about the Tester
from flask.ext.wtf import Form, TextField, RadioField, IntegerField, SelectField, SubmitField,validators, ValidationError

class InformationForm(Form):
    firstname = TextField("First Name",[validators.Required()])
    lastname = TextField("Last Name",[validators.Required()])
    gender = SelectField("Gender", choices = [(1,'Male'),(2,'Female')])
    age = IntegerField("Age")
    blindtype = SelectField("Blind Type",choices=[(1,'Congential'),(2,'Accidental'),(3,'Non-Blind')])
    email = TextField("Email",[validators.Required(),validators.Email()])
    contact = IntegerField("Contact",[validators.Required()])
    submit = SubmitField("Send")