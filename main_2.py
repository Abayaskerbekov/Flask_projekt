""" flask """

from flask import Flask

app= Flask(__name__)



@app.route("/ilgiz info")
def ilgiz2():
    return "My name is Ilgiz, I lived in Russian for a long time and recently moved to Bishkek, Ihave been living here for  6 months, i work here in yhe field of cars, i plan to stay for a long time"

@app.route("/my info")
def abdy2():
    return "My name is Abdyrazak, last name is Askerbekov. I am 17 years old, now I live in Bishkek."
@app.route("/about_me")
def abdy3():
    return "агай башка эч нерсе жаза албай койдум логика жок болуп жатат"
if __name__=='__main__':
    app.run(debug=True, )

