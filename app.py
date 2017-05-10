import api as AK
from data import get_senator
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

key = AK.key
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = key


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])


@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    print form.errors
    if request.method == 'POST':
        name = request.form['name']
        print name

    # if form.validate():
    #     # Save the comment here.
    #     senate = get_senator(name)
    # else:
    #     flash('All the form fields are required. ')

    senate = get_senator(name)

    return render_template('index.html', form=form, senate=senate)


if __name__ == "__main__":
    app.run()
