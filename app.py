import random 
from flask import Flask, render_template, session, request, redirect 
from services import country_service

app = Flask(__name__)
app.secret_key = 'thisShouldBeASecret'

@app.route('/')
def index():
    countries_and_capitals = country_service.fetch_countries_and_capitals()
    random.shuffle(countries_and_capitals)
    
    country_capital = random.choice(countries_and_capitals)
    session['country'] = country_capital[0]
    session['capital'] = country_capital[1]
     
    return render_template("index.html", country=session['country'])

@app.route('/guess', methods=['POST'])
def result():
    if not request.form["guess"] or not request.form["guess"].strip():
        error = 'name is missing' 
        return render_template("index.html", country=session['country'])

    if request.form["guess"].casefold() == str(session['capital']).casefold():
        answer = "Correct, the capital is "+ session['capital']
        return render_template("index.html", country=session['country'], answer=answer) 

    else:
        answer = "wrong, the capital is: "+ session['capital']
        return render_template("index.html", country=session['country'], answer=answer)
    
if __name__ == "__main__":
    app.run(debug=True)