from flask import Flask
from flask import jsonify
import whois
import datetime

app = Flask(__name__)

@app.route("/<domain>")
def lookup(domain):
	w = whois.whois(domain)
	
	return (w)