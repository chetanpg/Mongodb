#======================================================================================================================
#Author: chetan Gavankar
#Goal:   Mongodb connect class
#        This program will inititiate Mongoconnect class by passing  user,password,server,port and db name
#        and inserts data into Mongodb
#=======================================================================================================================
from __future__ import print_function
from pprint import pprint
from Classes.class_mongo_connect import Mongoconnect
import pymongo

def dbconn():
    #this information can be recevied from screen or in a file or as a command line
    # parameters.For simplicity it is hardcoded in this sample program
    userid="admin"
    pswd="password"
    server="localhost"
    port="27017"
    dbname="test"

    #try block to exit if connection error
    try:
      o = Mongoconnect(userid,pswd,server,port,dbname)
      db=o.dbconnect()
    except:
      print("Connection error , please provide correct information")
      quit()
    return db

#insert one record at a time
def insonerec(db):
    #set the collection , in this case Cars
    collection = "cars"
    Collection= db[collection]
    #set the record to be inserted
    rec={"Fname":"John","Lname":"Macmilan","City":"New York","Country":"USA"}
    try:
      Collection.insert_one(rec)
      print("One Record Inserted Successfully")
    except:
      print("Record Not Inserted , Some error encountered")
      quit()
    return

#insert multiple records in one insert command
def insmultrec(db):
    #set the collection , in this case Cars
    collection = "cars"
    Collection= db[collection]
    #set the records to be inserted
    rec1={"Fname":"Mini","Lname":"manu","City":"Chicago","Country":"USA"}
    rec2={"Fname":"Roger","Lname":"Federal","City":"Chicago","Country":"USA"}
    #set list of records
    records=[rec1,rec2]
    try:
      Collection.insert_many(records,ordered=False)
      print("All Records Inserted Successfully")
    except:
      print("Records Not Inserted , Some error encountered")
      quit()
    return

if __name__ == '__main__':
    db=dbconn()
    insonerec(db)
    insmultrec(db)
    quit()
