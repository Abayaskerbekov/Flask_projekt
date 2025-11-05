""" flask """

from flask import Flask

app= Flask(__name__)


@app.route('/')
def hello():
    return ('hello world    ')

@app.route("/about_me")
def about_me():
    return "my name is Abdy"
@app.route("/my info")
def askarov():
    return "Askerbekov Abdyrazzak Marsovich \nFull Code IT Academy\ncity: Bishkek"

if __name__=='__main__':
    app.run(debug=True, )