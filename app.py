from flask import Flask, render_template, request
from geopy.geocoders import Nominatim
import pandas as pd
import geocoder

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    return render_template('start.html')

@app.route('/results/<lat>,<lng>')
def results(lat, lng):
    df = pd.read_csv('static/404.csv')
    a = len(df[(float(lat)-0.027 <= df['lat']) & (df['lat'] <= float(lat)+0.027) & (float(lng)-0.025 <= df['lon']) & (df['lon'] <= float(lng)+0.025)])
    send="MEDIUM"
    clr="#5E17EB"
    if a>500:
        send="HIGH"
        clr="red"
    elif a<200:
        send="LOW"
        clr="green"
    
    return render_template('results.html', num=str(a), send=send, clr=clr, lmao = [lat,lng])

@app.route('/measures')
def measures():
    return render_template('measures.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/geolol')
def geolol():
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode("Andheri Mumbai")
    print(getLoc.address)
    print("Latitude = ", getLoc.latitude, "\n")
    print("Longitude = ", getLoc.longitude)
    return render_template('geo.html', lat=getLoc.latitude,lng= getLoc.longitude )

@app.route('/curloc')
def curloc():
    g = geocoder.ip('me')
    print(g.latlng)
    return render_template('geo.html', lat=g.latlng[0],lng= g.latlng[1] )

@app.route('/read')
def read():
    df = pd.read_csv('static/404.csv')
    print(len(df[(70 <= df['lon']) & (df['lon'] <= 100)]))
    return render_template('geo.html')
if __name__ == "__main__":
    app.run(debug=True)