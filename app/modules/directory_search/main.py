from app import app
from db_setup import init_db, db_session
from forms import PersonSearchForm
from flask import flash, render_template, request, redirect
# from [database] import database class

init_db()


@app.route('/', methods=['GET', 'POST'])
def index():
    search = PersonSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
 
    return render_template('index.html', form=search)
 
 
@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
 
    if search.data['search'] == '':
        qry = db_session.query() # Database query class name
        results = qry.all()
 
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        return render_template('results.html', results=results)
 
if __name__ == '__main__':
    app.run()