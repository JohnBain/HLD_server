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
	
	return finaljson

@app.route('/list_user_items', methods=['POST']) #direct POST request
def lui():
	(cursor, cnx) = open_connection()
	query = "SELECT * from Items WHERE UserId = 1"
	cursor.execute(query)
	row = cursor.fetchone()
	finaljson = []
	while row is not None:
		itm = dict(zip(cursor.column_names, row))
		finaljson.append(itm)
		row = cursor.fetchone()

	close_connection(cnx)
	return finaljson

#curl -X POST -H "Content-Type: application/json" -d '{"productId": 123456, "quantity": 100}' http://3.88.151.187:5000/add_user_item

@app.route('/add_user_item', methods=['POST'])
def aui():
    myjson = request.get_json(force=True) #forgot to set MIME type... remove in production
    for i in myjson:
    	print(myjson)
    (cursor, cnx) = open_connection()
    query = "INSERT INTO Items (UserID,imageUrl) VALUES (1, 'https://i.pinimg.com/736x/44/29/f0/4429f02128255f000ff0f11e03fc2cb2.jpg');"
    cursor.execute(query)
    cnx.commit()
    return "Done!"

@app.route('/create_new_user', methods=['POST'])
def cnu():
    myjson = request.get_json(force=True) 
    for i in myjson:
    	print(myjson)
    (cursor, cnx) = open_connection()
    query = "INSERT INTO Items (UserID,imageUrl) VALUES (1, 'https://i.pinimg.com/736x/44/29/f0/4429f02128255f000ff0f11e03fc2cb2.jpg');"
    cursor.execute(query)
    cnx.commit()
    return "Done!"

if __name__ == "__main__":
	app.run('0.0.0.0', 5000, use_reloader=True)




