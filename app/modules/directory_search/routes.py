import mimetypes
from app import app
from app.modules.directory_search.forms import PersonSearchForm
from app.modules.directory_search import blueprint, helpers
from app.modules.profile.helpers import serialize_positions, serialize_courses
from app.models import User, Profile, Course, Position, Production
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
    first_name = search.data['first_name']
    last_name = search.data['last_name']

    # Somehow search for the name
    if search.data['select'] == 'All':
        # Re-search if both fields are empty
        if first_name == '' and last_name == '':
            flash('Please specify either a name or a role')
            return redirect(url_for('directory_search.index'))
        # TODO: Query all searches with the name
    else:
        role = search.data['select']
        if search.data['first_name'] == '':
            # TODO: Query all searches of the role
            '''
            qry = db_session.query() # Database query class name
            results = qry.all()
            '''
            pass
        else:
            # TODO: Query search of role and name
            pass

    # If there are no results
    if not results:
        flash('No results found!')
        return redirect(url_for('directory_search.index'))

    # Either view the user
    return render_template('results.html', results=results)

@blueprint.route('/directory_search/users/<int:user_id>')
def view_user(user_id):
    user = User.query.get(int(user_id))
    profile = user.profile[0]
    positions = profile.positions
    courses = profile.courses
    return render_template('user_profile.html', user=user, profile=profile, positions=serialize_positions(positions), courses=serialize_courses(courses))

@blueprint.route('/directory_search/users/<int:user_id>/image')
def get_image(user_id):
    # Have some safety check that calls flask.abort(401)?
    extension, image = helpers.get_image(user_id)
    response = flask.make_response(image)
    response.headers.set('Content-Type',
                         mimetypes.guess_type('img.' + extension)[0])
    return response

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
