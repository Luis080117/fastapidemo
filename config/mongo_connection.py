from mongoengine import *

def connect_to_mongodb(database_name, collection_name):
    connection = connect(db=database_name, host='localhost', port=27017)
    return connection

def disconnect_from_mongodb():
    return disconnect()