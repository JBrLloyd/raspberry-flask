from flask import Flask, request, render_template
from flask import Blueprint


home_blueprint = Blueprint('home', __name__, template_folder='./templates')


@home_blueprint.route('/', methods=['GET'])
def index():
  return render_template('index.html')
