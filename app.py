from flask import Flask, request
app = Flask(__name__)

import datetime
import mysql.connector
import json
from functools import wraps


def dbconnection(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        cnx = mysql.connector.connect(user='hauld', database='Hauld', host='localhost', password='SuWoo123')
        cursor = cnx.cursor()
        print("Connection opened")
        # getting the returned value
        output = f(*args,cursor=cursor,cnx=cnx)
        cnx.commit()
        cnx.close()
        print("Connection closed")
        return output
    return decorated_function


 
# def open_connection():
#     cnx = mysql.connector.connect(user='hauld', database='Hauld', host='localhost', password='SuWoo123')
#     cursor = cnx.cursor()

#     return (cursor, cnx)

# def close_connection(cnx):
#     print('close connection!')
#     cnx.close()



"""
@app.route('/add_item', methods=['POST']) #direct POST request
def add_item():
	query = "INSERT INTO Items (UserID,imageUrl) VALUES (1, 'randomimage.jpg')"
 	cursor.execute(query)
 		return "<h1>Hello world!</h1>"
"""
@app.route('/hello_world', methods=['GET'])
def hello_world():
    return "<h1>Hello world!</h1>"

#curl http://3.88.151.187:5000/list_items
@app.route('/list_items', methods=['GET']) #direct POST request
@dbconnection
def list_items(**kwargs):
	print('in list items')
	cursor = kwargs['cursor']
	cnx = kwargs['cnx']
	query = "SELECT * from Items"
	result = cursor.execute(query)
	row = cursor.fetchone()
	finaljson = []
	while row is not None:
		itm = dict(zip(cursor.column_names, row))
		finaljson.append(itm)
		row = cursor.fetchone()

	# close_connection(cnx)
	
	return finaljson, 200

@app.route('/list_users', methods=['GET']) #direct POST request
@dbconnection
def list_users(**kwargs):
	print('in list users')
	cursor = kwargs['cursor']
	cnx = kwargs['cnx']
	query = "SELECT * from Users"
	result = cursor.execute(query)
	row = cursor.fetchone()
	finaljson = []
	while row is not None:
		itm = dict(zip(cursor.column_names, row))
		finaljson.append(itm)
		row = cursor.fetchone()

	# close_connection(cnx)
	
	return finaljson, 200

#curl -d '{"userId":"1"}' -H "Content-Type: application/json" -X POST http://3.88.151.187:5000/list_items_by_user
@app.route('/list_items_by_user', methods=['POST']) #direct POST request
@dbconnection
def libu(**kwargs):
	print(request.json)
	if not "userId" in request.json:
		return "Bad Request - JSON does not contain userId", 400
	userId = request.json['userId']
	(cursor, cnx) = (kwargs['cursor'], kwargs['cnx'])
	query = f"SELECT * from Items WHERE UserId = {int(userId)}"
	cursor.execute(query)
	row = cursor.fetchone()
	finaljson = []
	while row is not None:
		itm = dict(zip(cursor.column_names, row))
		finaljson.append(itm)
		row = cursor.fetchone()

	return finaljson, 200

#curl -d '{"userId":"1", "imagePath":"p.jpg"}' -H "Content-Type: application/json" -X POST http://3.88.151.187:5000/add_user_item
@app.route('/add_user_item', methods=['POST'])
@dbconnection
def aui(**kwargs):
    (cursor, cnx) = (kwargs['cursor'], kwargs['cnx'])
    if not all(key in request.json for key in ('userId', 'imagePath')):
        return "Failed!"
    (userId,imagePath) = (int(request.json['userId']), request.json['imagePath'])
    query = f"INSERT INTO Items (UserID,imageUrl,createdOn,updatedOn) VALUES ({userId}, '{imagePath}', CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP());"
    cursor.execute(query)
    return f"Successfuly created new imageUrl {imagePath} on user {userId}!", 200

#curl -d '{"username": "jimbob", "pword": "jimothy"}' -H "Content-Type: application/json" -X POST http://3.88.151.187:5000/create_new_user
@app.route('/create_new_user', methods=['POST'])
@dbconnection
def cnu(**kwargs):
	(cursor, cnx) = (kwargs['cursor'], kwargs['cnx'])
	myjson = request.get_json(force=True) 
	print(request.json)
	if not all(key in request.json for key in ('username', 'pword')):
		return "Bad JSON", 400
	username = request.json['username']
	pword = request.json['pword']

	query = f"SELECT * from Users where username='{username}'"

	result = cursor.execute(query)
	row = cursor.fetchone()
	finaljson = []
	if row is None:
		#proceed
		print('it worked')
	else:
		return f"User {username} already exists", 500

	query = f"INSERT INTO Users (username,pword) VALUES ('{username}', '{pword}');"
	result = cursor.execute(query)
	row = cursor.fetchone()
	finaljson = []
	while row is not None:
		itm = dict(zip(cursor.column_names, row))

	cnx.commit()
	return f"User {username} added!", 200	

if __name__ == "__main__":
	app.run('0.0.0.0', 5000, use_reloader=True)



