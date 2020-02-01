from app import app
from app.modules.directory_search.forms import PersonSearchForm
from app.modules.directory_search import blueprint
from flask import flash, render_template, request, redirect, url_for
# from [database] import database class

#init_db()

@blueprint.route('/directory_search', methods=['GET', 'POST'])
def index():
    search = PersonSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('directory_search.html', form=search)


@blueprint.route('/directory_search/results')
def search_results(search):
    results = []
    search_string = search.data['name']

    # Somehow search for the name
    if search.data['name'] == '':
        qry = db_session.query() # Database query class name
        results = qry.all()

    # If there are no results
    if not results:
        flash('No results found!')
        return redirect(url_for('directory_search.index'))
    else:
        # display results
        return render_template('results.html', results=results)

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)

