from flask import Flask, render_template, request, escape
from vsearch import search_for_letters

from src.ch10.checker import check_login

LOG_FILE_NAME = 'vsearch.txt'

appl = Flask(__name__)


@appl.route('/get_author')
@check_login
def get_author() -> str:
    return 'siliwen is the author'


@appl.route('/search', methods=['POST'])
@check_login
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
@check_login
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search on the web!')

@appl.route('/viewlog')
@check_login
def viewlog() -> str:
    log_content = []
    with open(LOG_FILE_NAME) as log:
        for line in log.readlines():
            items = list(map(lambda x : escape(x), line.split('|')))
            log_content.append(items)
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html', the_title='View Log',
                    the_row_titles=titles, the_data=log_content, )


def log_request(req: 'flask_request', res: str) -> None:
    with open(LOG_FILE_NAME, 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

if __name__ == '__main__':
    appl.run(debug=True)
