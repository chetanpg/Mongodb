#======================================================================================================================
#Author: chetan Gavankar
#Goal:   Mongodb connect class
#        This program will inititiate Mongoconnect class by passing  user,password,server,port and db name
#=======================================================================================================================
from __future__ import print_function
from pprint import pprint
from Classes.class_mongo_connect import Mongoconnect
import pymongo

#this information can be recevied from screen or in a file or as a command line
# parameters.For simplicity it is hardcoded in this sample program
#program is tested using local Mongodb server but you can change these values as required 

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

#set the collection , in this case Cars
collection = "cars"
Collection= db[collection]
#set the query , in this case it is empty but this is the place to set the query needed
query={}
#use limit / sort on cursor as needed
cursor=Collection.find(query).limit(2)
for doc in cursor:
      for key,value in doc.items():
         print("key:%s,Value:%s" %(key,value))
quit()
