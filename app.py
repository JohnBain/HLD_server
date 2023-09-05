from flask import Flask, request
app = Flask(__name__)

import datetime
import mysql.connector
import json

# def connect_decorator(func):
#     def inner1(*args, **kwargs):
         
#         print("before Execution")
#         cnx = mysql.connector.connect(user='hauld', database='Hauld', host='localhost', password='SuWoo123')
#         cursor = cnx.cursor()
#         # getting the returned value
#         returned_value = func(*args, **kwargs)
#         print("after Execution")
#         cnx.close()
#         # returning the value to the original frame
#         return returned_value
         
#     return inner1
 
def open_connection():
    cnx = mysql.connector.connect(user='hauld', database='Hauld', host='localhost', password='SuWoo123')
    cursor = cnx.cursor()

    return (cursor, cnx)

def close_connection(cnx):
    print('close connection!')
    cnx.close()



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
def list_items():
	print('in list items')
	(cursor, cnx) = open_connection()
	query = "SELECT * from Items"
	result = cursor.execute(query)
	row = cursor.fetchone()
	finaljson = []
	while row is not None:
		itm = dict(zip(cursor.column_names, row))
		finaljson.append(itm)
		row = cursor.fetchone()

	close_connection(cnx)
	
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

@app.route('/add_user_item', methods=['POST'])
def aui():
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




