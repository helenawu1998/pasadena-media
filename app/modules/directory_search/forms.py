from wtforms import Form, StringField, SelectField
# from app.modules.directory_search.templates.directory_search import loadFilter

# Credit to http://www.blog.pythonlibrary.org/2017/12/13/flask-101-how-to-add-a-search-form/
class PersonSearchForm(Form):

	# # (value, label)
    # choices = [('All', 'All'),
    #    		   ('Director', 'Director'),
    #    		   ('Technical Director', 'Technical Director'),
    #            ('Actor', 'Actor'),
    #            ('Cameraman', 'Cameraman'),
    #            ('Editor', 'Editor'),
    #            ('Musician', 'Musician'),
    #            ('Any', 'Any')]
    # select = SelectField('Search for role:', choices=choices)
    print("HELLO")
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    # roles = directory_search.loadFilter('rolesUL')
    # classes = directory_search.loadFilter('classesUL')
