import requests
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def covid19():
    url = "https://static.easysunday.com/covid-19/getTodayCases.json"
    result = json.loads(requests.get(url).text)
    return render_template('index.html', result=result)

@app.route("/province")
def province():
    url1 = "https://covid19.ddc.moph.go.th/api/Cases/today-cases-by-provinces"
    result1 = json.loads(requests.get(url1).text)
    return render_template('province.html',result1=result1)

@app.route("/ripple3")
def ripple3():
    url2 = "https://covid19.ddc.moph.go.th/api/Cases/timeline-cases-all"
    result2 = json.loads(requests.get(url2).text)
    return render_template('ripple3.html',result2=result2)

@app.route("/ripple1-2")
def ripple12():
    url3 = "https://covid19.ddc.moph.go.th/api/Cases/round-1to2-all"
    result3 = json.loads(requests.get(url3).text)
    return render_template('ripple1-2.html',result3=result3)

@app.route("/world.countries")
def world():
    url4 = "https://coronavirus-19-api.herokuapp.com/countries"
    result4 = json.loads(requests.get(url4).text)
    return render_template('worldct.html',result4=result4)


