from flask import Flask, render_template, request, json, jsonify
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)


#MongoDb Configuration
client = MongoClient()
db=client.Bucketlist
accounts = db.accounts

#storing user credentials
def store_user(user_name, user_username, user_password):
   if accounts.find_one({"name": user_name}) is None :
       user = {"name": user_name,
            "username":user_username,
            "password":user_password}

       post_id = accounts.insert_one(user).inserted_id
       return 0
   else:
       return "User exists!"


@app.route('/')
def main():
        return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
        return render_template('signup.html')


@app.route('/signUp', methods=['POST'])
def signup():
    _name=request.form['inputName']
    _email=request.form['inputEmail']
    _password=request.form['inputPassword']

    if _name and _email and _password:

        #create the salted hash
        _hashed_password = generate_password_hash(_password)

        #store the user credentials
        data = store_user(_name, _email, _hashed_password)

        if data == 0:
            return json.dumps({'message':'User created succesfully!'})
        else:
            return json.dumps({'error': str(data)})


    else:
        return json.dumps('Enter the required field')


if __name__ == "__main__":
    app.run()


