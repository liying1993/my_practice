import random
from flask import Flask, render_template, flash, redirect, url_for, session
from flask_wtf import Form
from wtforms.validators import Required, NumberRange
from flask_bootstrap import Bootstrap
from wtforms import IntegerField, SubmitField

app = Flask(__name__)
app.config["SECRET_KEY"] = "my name is liying"
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    session["number"] = random.randint(0,1000)
    session["times"] = 10
    return render_template("index.html")

@app.route('/guess', methods=["GET", "POST"])
def guess():
    times = session["times"]
    result = session.get("number")
    form = GuessNumberForm()
    if form.validate_on_submit():
        times -= 1
        session["times"] = times
        if times == 0:
            flash("you lose")
            return redirect(url_for("index"))
        answer = form.number.data
        if answer > result:
            flash("too big, you have %s remaining" % times)
        elif answer < result:
            flash("too small,you hava %s remaining" % times)
        else:
            flash("you win")
            return redirect(url_for("index"))
        return redirect(url_for("guess"))
    return render_template("guess.html", form=form)

class GuessNumberForm(Form):
    number = IntegerField(u"please input (0~1000):", validators=[
        Required("please input a solid"),
        NumberRange(0,1000,u"0~1000")
    ])
    submit = SubmitField("submit")

if __name__ == '__main__':
    app.run()
