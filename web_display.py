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
    msg = '{0} is available'.format((len(results_list)))
    if len(results_list) == 0:
        msg = 'There are no page has this content'

    content = dict()
    for file in results_list:
        content[file] = search_engine.readContent(file)

    return render_template('page-query.html', search_query=search_query, content=content, msg=msg)


if __name__ == '__main__':
    app.run(debug=True)