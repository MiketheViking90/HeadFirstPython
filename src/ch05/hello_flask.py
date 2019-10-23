from flask import Flask, render_template, request, escape
from vsearch import search_for_letters

LOG_FILE_NAME = 'vsearch.txt'

appl = Flask(__name__)


@appl.route('/get_author')
def get_author() -> str:
    return 'siliwen is the author'


@appl.route('/search', methods=['POST'])
def search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    res = str(search_for_letters(phrase, set(letters)))
    log_request(request, res)
    return render_template('results.html',
                           the_title = 'Here are your results: ',
                           the_phrase = phrase,
                           the_letters = letters,
                           the_results = res)

@appl.route('/')
@appl.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search on the web!')

@appl.route('/viewlog')
def viewlog() -> str:
    with open(LOG_FILE_NAME) as log:
        contents = escape(log.read())
    return contents


def log_request(req: 'flask_request', res: str) -> None:
    with open(LOG_FILE_NAME, 'a') as log:
        print(req, res, file=log)

if __name__ == '__main__':
    appl.run(debug=True)
