from flask import Flask, render_template
from vsearch import search_for_letters

appl = Flask(__name__)


@appl.route('/')
def hello() -> str:
    return 'Hello, I am running Python on a web app!'


@appl.route('/get_author')
def get_author() -> str:
    return 'siliwen is the author'


@appl.route('/search', methods=['POST'])
def search() -> str:
    return str(search_for_letters("life, the universe, and everything", set("eiru,!")))

@appl.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search on the web!')

appl.run(debug=True)
