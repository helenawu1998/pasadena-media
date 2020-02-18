import mimetypes
from app import app
from app.modules.directory_search.forms import PersonSearchForm
from app.modules.directory_search import blueprint, helpers
from app import db
from app.models import User, Profile, Course, Position, Production
# from app.models import Profile, Course, Position, Production
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
    first_name = search.data['first_name']
    last_name = search.data['last_name']
    classes = search.data['classes']
    roles = search.data['roles']

    # flash(type(db.session.query(Profile).filter(Profile.first_name == first_name)))
    # Somehow search for the name
    flash(search.data)
    if len(classes) and len(roles):
        classes = classes.split(',')[0]
        roles = roles.split(',')[0]
        users = db.session.query(Profile, Course, Position)
        for c in classes:
            users = users.filter(Course.course_name == c)
        for r in roles:
            users = users.filter(Position.position_name == r)
        if first_name == '' and last_name == '':
            # Query all people who have taken these classes with these roles
            # Already done above
            pass
        elif first_name == '':
            # Query last name
            users = users.filter(Profile.last_name == last_name)
        elif last_name == '':
            # Query first name
            users = users.filter(Profile.first_name == first_name)
        else:
            # Query both names
            users = users.filter(Profile.first_name == first_name)\
                        .filter(Profile.last_name == last_name)
    elif len(classes):
        classes = classes.split(',')[0]
        users = db.session.query(Profile, Course)
        for c in classes:
            users = users.filter(Course.course_name == c)
        if first_name == '' and last_name == '':
            # Query all people who have taken these classes with these roles
            # Already done
            pass
        elif first_name == '':
            # Query last name
            users = users.filter(Profile.last_name == last_name)
        elif last_name == '':
            # Query first name
            users = users.filter(Profile.first_name == first_name)
        else:
            # Query both names
            users = users.filter(Profile.first_name == first_name)\
                        .filter(Profile.last_name == last_name)
    elif len(roles):
        roles = roles.split(',')[0]
        for r in roles:
            users = users.filter(Position.position_name == r)
        if first_name == '' and last_name == '':
            # Query all people who have taken these classes with these roles
            # Already done
            pass
        elif first_name == '':
            # Query last name
            users = users.filter(Profile.last_name == last_name)
        elif last_name == '':
            # Query first name
            users = users.filter(Profile.first_name == first_name)
        else:
            # Query both names
            users = users.filter(Profile.first_name == first_name)\
                        .filter(Profile.last_name == last_name)
    else:
        if first_name == '' and last_name == '':
            flash('Please specify either a name or a role')
            return redirect(url_for('directory_search.index'))
        elif first_name == '':
            users = users.filter(Profile.last_name == last_name)
        elif last_name == '':
            users = users.filter(Profile.first_name == first_name)
        else:
            # TODO: Query search of role and name
            users = users.filter(Profile.first_name == first_name)\
                        .filter(Profile.last_name == last_name)

    # If there are no results
    if not users:
        flash('No results found!')
        return redirect(url_for('directory_search.index'))

    # Either view the user
    # if users.count() == 1:
        # return render_template('view_user.html', results=users) #, user_id=results[0].get_id())
    # else:
    users = users.all()
    return render_template('results.html', results=users)


@blueprint.route('/directory_search/users/<int:user_id>')
def view_user(user_id):
    user = helpers.get_user(user_id)
    return render_template('view_user.html', results=user, user_id=user_id)


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
