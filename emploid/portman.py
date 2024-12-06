from flask import Flask, render_template, url_for, request, redirect, session
import requests
from markupsafe import escape
import mysql.connector
from time import sleep
import os
import pathlib
file_path = os.path.dirname(os.path.abspath(__file__))+'/' 
file_path = pathlib.Path(__file__).parent.resolve()
print("File path:", file_path)


class Portman:

    def __init__(self, _port=1912, _db_host="localhost", _db_user="root", _db_password="", _db_database="", _db_connect=False):
        self.port = _port
        self.server = Flask(__name__)

        self.db_host = _db_host
        self.db_user = _db_user
        self.db_password = _db_password
        self.db_database = _db_database

        try:
            print("attempting to connect to database...")
            self.connect_to_database(self.db_host, self.db_user, self.db_password, self.db_database)
        except Exception as e:
            print("error when trying to connect to database")

    def connect_to_database(self, _db_host="localhost", _db_user="root", _db_password="", _db_database=""):

        self.db = mysql.connector.connect(
            host=_db_host,
            user=_db_user,
            password=_db_password,
            database=_db_database
        )

        if(self.db.connection_id):
            print("connected successfully to DB")
        else:
            raise Exception("could not connect to DB")

    def serve(self, _port="", _debug=False):

        if(_port):
            port = _port
        else:
            port = self.port
            
        print("running app...")
        if(_debug):
            self.server.run(host="0.0.0.0", port=port)
        else:
            if __name__ == "__main__":
                from waitress import serve
                serve(self.server, host="0.0.0.0", port=port)

    def add_endpoint(self, _name, _content):
        name = _name
        content = _content

        @self.server.get(name)
        def name():
            return content
        
    def query(self, _query, _values):
        
        query = _query
        action = None

        #0 commit, 1 fetch
        if("INSERT" in query or "DELETE" in query):
            action = 0
        if("SELECT" in query):
            action = 1
        
        mycursor = self.db.cursor()
        sql = query
        
        if(action==1):
            mycursor.execute(sql)
            result = mycursor.fetchall()

        if(action==0):
            values = _values
            mycursor.execute(sql, values)
            self.db.commit()
        
        return result
        
    def endpoint_insert(self):
        @self.server.get('/message/addMessage')
        def message_add():
            receipant = request.args.get('messageReceipant')
            content = request.args.get('messageContent')

            if(receipant and content):
                mycursor = mydb.cursor()
                sql = "INSERT INTO whatsapp_messages (messageReceipant, messageContent) VALUES (%s, %s)"
                val = (receipant, content)
                mycursor.execute(sql, val)
                self.db.commit()
                sleep(0.5)
                return "message added"
            else:
                return "error inserting null or empty value"

