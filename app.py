from flask import Flask
app = Flask(__name__)

import datetime
import mysql.connector

cnx = mysql.connector.connect(user='hauld', database='Hauld', host='localhost', password='SuWoo123')
cursor = cnx.cursor()

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
	query = "SELECT * from Items"
	cursor.execute(query)
	row = cursor.fetchone()
	finaljson = []
	while row is not None:
		itm = dict(zip(cursor.column_names, row))
		finaljson.append(itm)
		row = cursor.fetchone()

	cnx.close()
	return finaljson


if __name__ == "__main__":
	app.run('0.0.0.0', 5000, use_reloader=True)




# # for item in cursor:
# #   print(item)

# query = "SELECT * from Items"

# cursor.execute(query)

# for item in cursor:
#   print('here is item')
#   print(item)

# cnx.close()