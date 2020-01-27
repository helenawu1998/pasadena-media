from app import app

@app.route('/profile/<username>')
#@login_required
def profile():
    #user = User.query.filter_by(username=username).first_or_404()
    user = {'username'   : 'johnsmith',
            'email'      : 'johnsmith@gmail.com',
            'phone'      : '420-420-4204'
            'first_name' : 'John',
            'last_name'  : 'Smith',
            'position'   : 'Director'}
    return render_template('profile.html', user=user)
