#!/usr/bin/env python
# coding: utf-8

# In[75]:


from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,USER,PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 33179
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            if isinstance(data, dict):              # check if variable is a dictionary
                print('Created Succesfully')
                return True
            else:                                   # else it is false
                print('Invalid input, please try again')
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            return list(self.database.animals.find(data, {"_id": False}))  # Return data instead of printing
        else:
            return []
        
            
# Create method to implement the U in CRUD.
    def update(self, query, update_data):
        try:
            result = self.database.animals.update_many(query,{'$set':update_data})
            return result.modified_count
        except Exception as e:
            return 0
        
# Create method to implement the D in CRUD.
    def delete(self, removeData):
        if removeData:
            result = self.database.animals.delete_many(removeData)
            return result.deleted_count # Return the number of deleted records
        else:
            raise Exception("Nothing to delete, removeData is empty")





