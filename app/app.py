from typing import List, Dict
import simplejson as json
from flask import request, Response, redirect
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
from flask import Flask, flash, redirect, session, abort
import os

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'gradesDataFinal'
mysql.init_app(app)

# @app.route('/', methods=['GET'])
# def index():
#     user = {'username': 'Grades Project'}
#     cursor = mysql.get_db().cursor()
#     cursor.execute('SELECT * FROM grades')
#     result = cursor.fetchall()
#     return render_template('index.html', title='Home', user=user, grades=result)


@app.route('/view/<int:grades_id>', methods=['GET'])
def record_view(grades_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM grades WHERE id=%s', grades_id)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', grades=result[0])

@app.route('/edit/<int:grades_id>', methods=['GET'])
def form_edit_get(grades_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM grades WHERE id=%s', grades_id)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', grades=result[0])

@app.route('/edit/<int:grades_id>', methods=['POST'])
def form_update_post(grades_id):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('Lname'), request.form.get('Fname'), request.form.get('ssn'),
                 request.form.get('Test1'), request.form.get('Test2'),
                 request.form.get('Test3'), request.form.get('Test4'), request.form.get('Final'),
                 request.form.get('Grade'), grades_id)
    sql_update_query = """UPDATE grades t SET t.Last_name = %s, t.First_name = %s, t.SSN = %s, t.Test1 = 
        %s, t.Test2 = %s, t.Test3 = %s, t.Test4 = %s,t.Final= %s,t.Grade = %s  WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)

@app.route('/grades/new', methods=['GET'])
def form_insert_get():
    #checking if the session has a login valid, if valid then page gets loaded.
    if not session.get('logged_in'):
        return render_template('login.html')
    if session.get('logged_in'):
        return render_template('new.html', title='New Grades Form')

@app.route('/grades/new', methods=['POST'])
def form_insert_post():
    cursor = mysql.get_db().cursor()
    inputData = (
    request.form.get('Lname'), request.form.get('Fname'), request.form.get('ssn'), request.form.get('Test1'),
    request.form.get('Test2'), request.form.get('Test3'), request.form.get('Test4'), request.form.get('Final'),
    request.form.get('Grade'))
    sql_insert_query = """INSERT INTO grades (Last_name,First_name,SSN,Test1,Test2,Test3,Test4,Final,Grade) VALUES (%s, %s,%s, %s,%s, %s,%s,%s,%s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)

@app.route('/delete/<int:grades_id>', methods=['POST'])
def form_delete_post(grades_id):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM grades WHERE id = %s """
    cursor.execute(sql_delete_query, grades_id)
    mysql.get_db().commit()
    return redirect("/", code=302)

@app.route('/api/v1/grades', methods=['GET'])
def api_browse() -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM grades')
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp

@app.route('/api/v1/grades/<int:grade_id>', methods=['GET'])
def api_retrieve(grade_id) -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM grades WHERE id=%s', grade_id)
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp

@app.route('/api/v1/grades/<int:grades_id>', methods=['PUT'])
def api_edit(grades_id) -> str:
    cursor = mysql.get_db().cursor()
    content = request.json
    inputData = (content['Last_name'], content['First_name'], content['SSN'],
                 content['Test1'], content['Test2'],
                 content['Test3'], content['Test4'],content['Final'], content['Grade'],grades_id)
    sql_update_query = """UPDATE grades t SET t.Last_name = %s, t.First_name = %s, t.SSN = %s, t.Test1 = 
        %s, t.Test2 = %s, t.Test3 = %s, t.Test4 = %s,t.Final= %s,t.Grade = %s  WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp

@app.route('/api/v1/grades', methods=['POST'])
def api_add() -> str:

    content = request.json

    cursor = mysql.get_db().cursor()
    inputData = (content['Last_name'], content['First_name'], content['SSN'],
                 content['Test1'], content['Test2'],
                 content['Test3'], content['Test4'], content['Final'], content['Grade'])
    sql_insert_query = """INSERT INTO grades (Last_name,First_name,SSN,Test1,Test2,Test3,Test4,Final,Grade) VALUES (%s, %s,%s, %s,%s, %s,%s,%s,%s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    resp = Response(status=201, mimetype='application/json')
    return resp

@app.route('/api/v1/grades/<int:grades_id>', methods=['DELETE'])
def api_delete(grades_id) -> str:
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM grades WHERE id = %s """
    cursor.execute(sql_delete_query, grades_id)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp

# Final Assignment features *Karan Ramani*
# Login sessions

#Below code makes login required to access the main page of the site
@app.route('/')
def homepage():
    if not session.get('logged_in'):
        return render_template('login.html')
    if session.get('logged_in'):
        user = {'username': 'Grades Project'}
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM grades')
        result = cursor.fetchall()
        return render_template('index.html', title='Home', user=user, grades=result)

#login session by identifying the user inputs
@app.route('/grades/login', methods=['POST'])
def do_admin_login():
    password = request.form['password']
    username = request.form['username']
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM login WHERE username = %s AND password = %s', (username, password))
    userprofile = cursor.fetchone()
    if userprofile:
        session['logged_in'] = True
    else:
        flash('wrong password!')
        return homepage()
    return homepage()


#new user creation session
@app.route('/grades/new-user', methods=['GET'])
def form_insert_get_user():
    if not session.get('logged_in'):
        return render_template('login.html')
    if session.get('logged_in'):
        return render_template('new-user.html', title='New User Form')

#updating new user information to database using POST method
@app.route('/grades/new-user', methods=['POST'])
def form_insert_post_user():
    cursor = mysql.get_db().cursor()
    inputData = (
    request.form.get('Fname'), request.form.get('Lname'), request.form.get('username'), request.form.get('password'), request.form.get('email'))
    sql_insert_query = """INSERT INTO login (firstname, lastname, username, password, email) VALUES (%s, %s,%s, %s, %s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)

#logout of the session:
@app.route("/grades/logout")
def logout():
    session['logged_in'] = False
    return homepage()

# @app.route('/grades/login', methods=['GET'])
# def form_insert_get_login():
#     return render_template('login.html', title='Login')

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', debug=True)

