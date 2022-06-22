from flask import Flask, Response, render_template, request
from app.search_engine import SearchEngine
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home_page.html')

@app.route('/page-query', methods=['POST'])
def results():
    search_engine = SearchEngine()
    search_query = request.form.get('search_query')
    results_list = search_engine(search_query)
    total_results = 0
    for result in results_list:
        total_results += result[1]

    msg = f'Total result in page {total_results}'

    if len(results_list) == 0:
        msg = 'There are no page has this content'

    return render_template('page-query.html', search_query=search_query, content=results_list, msg=msg)


if __name__ == '__main__':
    app.run(debug=True)