from wtforms import Form, StringField, SelectField
from flask import request, jsonify, render_template
import sys
# from app.modules.directory_search.templates.directory_search import loadFilter
def classes_and_roles():
    if request.method == "POST":
        data = []
        data['title'] = request.json['title']
        print(data, file=sys.stderr)
        return jsonify(data)
    else:
        return render_template('directory_search.html')

# Credit to http://www.blog.pythonlibrary.org/2017/12/13/flask-101-how-to-add-a-search-form/
class PersonSearchForm(Form):
	# (value, label)
  '''
  choices = [('All', 'All'),
     		   ('Director', 'Director'),
     		   ('Technical Director', 'Technical Director'),
             ('Actor', 'Actor'),
             ('Cameraman', 'Cameraman'),
             ('Editor', 'Editor'),
             ('Musician', 'Musician'),
             ('Any', 'Any')]
  select = SelectField('Search for role:', choices=choices)
'''
  first_name = StringField('First Name')
  last_name = StringField('Last Name')
  roles = StringField('Roles (separated by commas)')
  classes = StringField('Classes (separated by commas)')
