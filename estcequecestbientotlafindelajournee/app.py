import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    now = datetime.datetime.now()
    texts = {
        now.hour >= 0 and now.hour < 9: (
            "L'avenir appartient à ceux qui se lèvent tôt.",
            "Nan, c'est une blague.",
        ),
        now.hour >= 9 and now.hour < 11: (
            "Non, mais c'est l'heure d'aller a la machine à café.",
            "",
        ),
        now.hour >= 11 and now.hour < 12: (
            "C'est l'heure de l'apéro !",
            "Et c'est presque mieux que la fin de la journée.",
        ),
        now.hour >= 12 and now.hour < 14: (
            "Ou tu continues l'apéro, ou tu vas manger",
            "Mais va falloir prendre une décision.",
        ),
        now.hour >= 14 and now.hour < 16: (
            "Si t'es gilet jaune, oui.",
            "",
        ),
        now.hour >= 16 and now.hour < 18: (
            "Nan, mais c'est tout comme.",
            "",
        ),
        now.hour >= 18: (
            'Rentre chez toi, on est au 35h ici...',
            "",
        ),
    }
    text, second_text = texts[True]
    return render_template('index.html', text=text, second_text=second_text)
