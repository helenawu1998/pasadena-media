from wtforms import Form, StringField, SelectField

# Credit to http://www.blog.pythonlibrary.org/2017/12/13/flask-101-how-to-add-a-search-form/
class PersonSearchForm(Form):
	# (value, label)
    choices = [('Director', 'Director'),
               ('Actor', 'Actor'),
               ('Cameraman', 'Cameraman'),
               ('Editor', 'Editor'),
               ('Musician', 'Musician')]
    select = SelectField('Search for role:', choices=choices)
    name = StringField('Name')
