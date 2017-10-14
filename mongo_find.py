#======================================================================================================================
#Author: chetan Gavankar
#Goal:   Mongodb connect class
#        This program will inititiate Mongoconnect class by passing  user,password,server,port and db name
#        and find the record from Mongodb
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

def findrec(db):
    #set the collection , in this case Cars
    collection = "cars"
    Collection= db[collection]
    #set the query , in this case it is empty but this is the place to set the query needed
    query={}
    #use limit / sort on cursor as needed
    cursor=Collection.find(query).limit(10)
    sanity = 0
    for doc in cursor:
          print("-------Record--------")
          for key,value in doc.items():
             print("key:%s,Value:%s" %(key,value))
    return

if __name__ == '__main__':
    db=dbconn()
    findrec(db)
    quit()
