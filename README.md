# pasadena-media
Web application for the non-profit Pasadena Media featuring a customized directory service.

# Setting up your environment
- Clone this repository. 
- Create virtual environment named venv at top-level of this directory.
```
python3 -m venv venv
```
- Activate virtual environment. Do this every time you work on this app. 
```
source venv/bin/activate
```
- Install requirements into the virtual environment.
```
pip install -r requirements.txt
```

# Database
- Development: SQLite (with Flask-SQLAlchemy)

# Testing
- For now, run app locally and visit localhost:5000.
```
flask run
```
