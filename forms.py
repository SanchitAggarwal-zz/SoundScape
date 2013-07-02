#Creating python form for information about the Tester


from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField

class InformationForm(Form):
    name=TextField("Name")
    email=TextField("Email")
    submit = SubmitField("Send")