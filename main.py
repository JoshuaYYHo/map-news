from flask import Flask, render_template, url_for, jsonify, request
from query_news import get_items, get_iso_country_code
import sqlite3
from datetime import date
from country_facts import country_info


app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("country_news.db")
    conn.row_factory = sqlite3.Row
    return conn

def grab_news(iso_code):
    conn = get_db_connection()
    c = conn.cursor()
    news = c.execute("SELECT news FROM country WHERE iso = ?", (iso_code,)).fetchone()
    conn.close()
    return news


def set_news(api_call, iso_code):
    conn = get_db_connection()
    c = conn.cursor()

    c.execute("UPDATE country SET news = ? WHERE iso = ?", (api_call, iso_code))

    conn.close()
    return True

def check_date(d):
    if d == date.today():
        return True
    return False

@app.route("/")
def home():
    return render_template("home.html")

# When returned it's the country name
@app.route("/country/<country_name>")
def country(country_name):
    # put the query_news functions

    # Be Careful w/ this API request
    country_news = get_items(country_name)
    country_iso_code = get_iso_country_code(country_name)

    #if not today's date, make the API call, otherwise grab from database

    #set_news(country_news, country_iso_code)
    # So if this was already queried, you don't have to do another API request
    
    #country_news = grab_news(country_iso_code)
    info = country_info(country_iso_code)
    
    return render_template("country.html", country_name=country_name, country_news=country_news, info=info)

#Handles the country route when you click the button popup
@app.route("/handle_country", methods=['POST'])
def handle_country():
    data = request.get_json()
    country_name = data.get('country_name')
    print(f"Selected country: {country_name}")
    # Redirect to the country route
    return jsonify({'redirect_url': url_for('country', country_name=country_name)})


if __name__ == "__main__":
    app.run(debug=True)