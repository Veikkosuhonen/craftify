from flask import render_template, request, redirect, session, abort, flash

from app import app, db
import shop

@app.route("/")
def index():
    return render_template("index.html", shops=shop.getShops())
