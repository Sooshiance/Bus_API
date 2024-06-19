from flask import Flask, request, jsonify
import requests


app = Flask(__name__)


# TODO : If owner wants to check which product is not in the store
@app.route('active-product/', methods=['GET'])
def getActiveProduct():
    data = requests.get("http://127.0.0.1:8000/api/")

    jdata = data.json()

    return jsonify(jdata)


# TODO : If owner wants to check his daily transactions
@app.route('daily-transactions/', methods=['GET'])
def dailyTransactions():
    pass


# TODO : If owner wants to check all messages from his/her customers
@app.route('read-comments/', methods=['GET'])
def readComments():
    pass


# TODO : If owner wants to combine all functions above and needs a report
@app.route('daily-report/', methods=['GET'])
def generateJournal():
    pass


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
