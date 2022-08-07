from crypt import methods
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, Flask!'

@app.route('/api/v1/getdetails',methods=['GET'])
def getAllInfo():
	data={"data":[{"name":"Hyatt Regency, Raipur","stars":"4","location":"Near Magneto Mall"},
	{"name":"Mattriot,Raipur","stars":"3.8","location":"Basti Road"},
	{"name":"Hotel Le Roi , Raipur","stars":"4.1","location":"Railway Station Road"}]}

	return jsonify(data)

if __name__ == '__main__':
	app.run(debug=True,ssl_context='adhoc')

