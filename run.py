from project import app

#main .py file 
#run run.py using following commands

# 1. export FLASK_APP=run.py
# 2. export FLASK_ENV=development
# 3. flask run

if __name__=='__main__':
    app.run(debug=True)