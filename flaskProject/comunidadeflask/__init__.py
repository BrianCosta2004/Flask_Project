from flask import Flask, render_template, request, flash, redirect, url_for
from forms import FormLogin, FormCriarConta
from flask_sqlalchemy import SQLAlchemy
from models import Usuario, Post

app = Flask(__name__)

lista_usuarios = ['Brian', 'Costa', 'Teste']

app.config['SECRET_KEY'] = 'dcc92759b404cc3d1adf6e83265a0d1e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db'

database = SQLAlchemy(app)