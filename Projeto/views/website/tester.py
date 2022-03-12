from cgitb import text
from flask import render_template, Blueprint

tester = Blueprint("tester", __name__)

@tester.route("/test", methods=["GET","POST"])
def test():
    return render_template("test.html", text="Le test")
