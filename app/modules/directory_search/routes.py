from app import app
from app.modules.directory_search.forms import PersonSearchForm
from app.modules.directory_search import blueprint
from flask import flash, render_template, request, redirect
# from [database] import database class

#init_db()


@blueprint.route('/directory_search', methods=['GET', 'POST'])
def index():
    search = PersonSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('directory_search.html', form=search)


@app.route('/directory_search/results')
def search_results(search):
    results = []
    search_string = search.data['name']

    if search.data['name'] == '':
        qry = db_session.query() # Database query class name
        results = qry.all()

    if not results:
        app.secret_key = 'super secret key'
        app.config['SESSION_TYPE'] = 'filesystem'

        #sess.init_app(app)
        flash('No results found!')
        return redirect('/directory_search')
    else:
        # display results
        return render_template('results.html', results=results)

if __name__ == '__main__':

    app.run(debug=True)
