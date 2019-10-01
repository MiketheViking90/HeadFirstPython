from flask import Flask
from vsearch import search_for_letters

appl = Flask(__name__)


@appl.route('/')
def hello() -> str:
    return 'Hello, I am running Python on a web app!'


@appl.route('/requests/get_author')
def get_author() -> str:
    return 'siliwen is the author'


@appl.route('/requests/search')
def search() -> str:
    return str(search_for_letters("life, the universe, and everything", set("eiru,!")))


appl.run()
