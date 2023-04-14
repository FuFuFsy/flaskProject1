"""
This module contains functions to update data both locally and remotely
"""
import json
import logging
from datetime import datetime

import pandas as pd


import auth, costants, data_storing

def update_one_record(info,date,nikename,condition={}):
    database = costants.DATABASE_NAME

    for collection in costants.COLLECTIONMESS:
        logging.info(
            f"\n- Updating '{collection}' from the MongoDB '{database}' database")
        collection_data = update_mongodb_collection(
            cluster_name=costants.CLUSTER_NAME, database_name=database,
            collection_name=collection, condition=condition,info=info,date=date,nikename=nikename
        )

# 按照条件删除记录
def update_mongodb_collection(cluster_name, database_name, collection_name,nikename,info,date,condition={}):
    """
    Reads from a MongoDB database a certain collection and if given querys with certain conditions.

    Args:
        - cluster_name (str): Name of the MongoDB cluster
        - database_name (str): Name of the MongoDB database
        - collection_name (str): Name of the MongoDB collection
        - condition (dict): Dictionary containing the conditions of the query.
        (EX: condition = {'name' : 'test'} gets all the documents of the collection
        that have 'name'='test')

    Returns:
        - (pymongo.cursor.Cursor): A pymongo Cursor object that is iterable and that
        represents the result of the query.
    """
    client = data_storing.connect_cluster_mongodb(
        cluster_name, auth.MONGODB_USERNAME, auth.MONGODB_PASSWORD)
    database = data_storing.connect_database(client, database_name)
    collection = data_storing.connect_collection(database, collection_name)[0]
    # logging.info(
    #     f"\n- Reading the '{collection_name}' collection in the '{database_name}' database")
    # collection.update_one(condition, { '$set': {"nikename": nikename, "info":info,"date":date}})
    return collection.update_one(condition, { '$set': {"nikename": nikename, "info":info,"date":date}})
