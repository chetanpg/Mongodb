#==============================================================
#Author    :- chetan Gavankar
#Goal      :- Mongodb connect class
#Usage     :- Mongoconnect(userid,pswd,server,port,dbname)
#Python 3  := in Python 2 import urllib and use urllib.quote_plus
#================================================================
from __future__ import print_function
from pprint import pprint
#
import pymongo
import urllib.parse


#class for opening Mongodb connection
#This Class has two methods one return DB connection
#and other return Instance Connection
class Mongoconnect(object):
   def __init__(self,user,password,server,port,dbname):

       self.user = user
       self.password = password
       self.server = server
       self.port = port
       self.dbname = dbname

#This method returns DB connection
   def dbconnect(self):
#use urllib.quote_plus for python 2
      pwd = urllib.parse.quote(self.password)
      url  = "mongodb://" + self.user + ":" + pwd + "@" + self.server + ":" + self.port + "/"
      print(url)
      connection = pymongo.MongoClient(url)
#to return object use [] and not connection.db which is string
      db = connection[self.dbname]
      return db

#This return Instance Connection
   def instconnect(self):
      pwd = urllib.quote_plus(self.password)
      url  = "mongodb://" + self.user + ":" + pwd + "@" + self.server + ":" + self.port + "/"
      connection = pymongo.MongoClient(url)
      return connection
