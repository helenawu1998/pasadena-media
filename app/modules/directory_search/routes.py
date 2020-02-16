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
    results = []
    first_name = search.data['first_name']
    last_name = search.data['last_name']
    classes = search.data['classes']
    roles = search.data['roles']

    # Somehow search for the name
    flash(search.data)
    if len(classes) and len(roles):
        if first_name == '' and last_name == '':
            # Query all people who have taken these classes with these roles
            users = Session.query(Course, Position)\
                        .filter(Course.course_name == classes)\
                        .filter(Position.production_name == roles).all()
        elif first_name == '':
            # Query last name
            users = Session.query(User, Course, Position)\
                        .filter(Course.course_name == classes)\
                        .filter(Position.production_name == roles)\
                        .filter(User.last_name == last_name).all()
        elif last_name == '':
            # Query first name
            users = Session.query(User, Course, Position)\
                        .filter(Course.course_name == classes)\
                        .filter(Position.production_name == roles)\
                        .filter(User.first_name == first_name).all()
        else:
            # Query both names
            users = Session.query(User, Course, Position)\
                        .filter(Course.course_name == classes)\
                        .filter(Position.production_name == roles)\
                        .filter(User.first_name == first>name)\
                        .filter(User.last_name == last_name).all()
    elif len(classes):
        if first_name == '' and last_name == '':
            # Query all people who have taken these classes with these roles
            users = Session.query(Course)\
                        .filter(Course.course_name == classes).all()
        elif first_name == '':
            # Query last name
            users = Session.query(User, Course)\
                        .filter(Course.course_name == classes)\
                        .filter(User.last_name == last_name).all()
        elif last_name == '':
            # Query first name
            users = Session.query(User, Course)\
                        .filter(Course.course_name == classes)\
                        .filter(User.first_name == first_name).all()
        else:
            # Query both names
            users = Session.query(User, Course)\
                        .filter(Course.course_name == classes)\
                        .filter(User.first_name == first>name)\
                        .filter(User.last_name == last_name).all()
    elif len(roles):
        if first_name == '' and last_name == '':
            # Query all people who have taken these classes with these roles
            users = Session.query(Position)\
                        .filter(Position.production_name == roles).all()
        elif first_name == '':
            # Query last name
            users = Session.query(User, Position)\
                        .filter(Position.production_name == roles)\
                        .filter(User.last_name == last_name).all()
        elif last_name == '':
            # Query first name
            users = Session.query(User, Position)\
                        .filter(Position.production_name == roles)\
                        .filter(User.first_name == first_name).all()
        else:
            # Query both names
            users = Session.query(User, Position)\
                        .filter(Position.production_name == roles)\
                        .filter(User.first_name == first>name)\
                        .filter(User.last_name == last_name).all()
    else:
        if first_name == '' and last_name == '':
            flash('Please specify either a name or a role')
            return redirect(url_for('directory_search.index'))
        elif first_name == '':
            users = Session.query(User).filter(User.last_name == last_name).all()
        elif last_name == '':
            users = Session.query(User).filter(User.first_name == first_name).all()
            # TODO: Query all searches of the role
            '''
            qry = db_session.query() # Database query class name
            results = qry.all()
            '''
        else:
            # TODO: Query search of role and name
            users = Session.query(User)\
                            .filter(User.first_name == first_name)\
                            .filter(User.last_name == last_name)

    # If there are no results
    if not results:
        flash('No results found!')
        return redirect(url_for('directory_search.index'))

    # Either view the user
    if len(results) == 1:
        return render_template('view_user.html') #, user_id=results[0].get_id())
    else:
        return render_template('results.html', results=results)


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
