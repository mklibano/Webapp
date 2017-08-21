from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient()
app = Flask(__name__)


#MongoDb Configuration
db=client.Bucketlist
accounts = db.accounts

#storing user credentials
def store_user(user_name, user_username, user_password):
   if accounts.find_one({"name": user_name}) is None :
       user = {"name": user_name,
            "username":user_username,
            "password":user_password}

       post_id = accounts.insert_one(user).inserted_id
       return post_id
   else:
       print("User exists!")


@app.route("/")
def main():
        return render_template('index.html')


if __name__ == "__main__":
    app.run()


