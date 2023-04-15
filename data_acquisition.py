"""
This module contains the functions used to acquire data both locally and remotely （fsy）message part
"""

import json
import logging
from datetime import datetime

import pandas as pd


import auth, costants, data_storing



#这个是读取货物数据库的
def acquire_data_from_message(conditionproduct={}):

    database = costants.DATABASE_NAME
    data = []

    for collection in costants.COLLECTIONMESS:
        logging.info(
            f"\n- Acquiring '{collection}' from the MongoDB '{database}' database")
        collection_data = read_mongodb_collection(
            cluster_name=costants.CLUSTER_NAME, database_name=database,
            collection_name=collection,condition=conditionproduct
        )
        #print(collection_data)
        for doc in collection_data:
            data.append(doc)
        # df_collection_data = pd.DataFrame(list(collection_data))
        # df_collection_data = df_collection_data.drop('_id', axis=1)
        #df_collection_data['Date'] = pd.to_datetime(df_collection_data['Date'])
        #df_collection_data = df_collection_data.set_index('Date')
        #data[collection] = df_collection_data

    return data

def acquire_rnum_from_message(condition={}):

    database = costants.DATABASE_NAME
    data = []

    for collection in costants.COLLECTIONMESS:
        logging.info(
            f"\n- Acquiring  '{collection}' record num from the MongoDB '{database}' database")
        collection_num = get_record_num(
            cluster_name=costants.CLUSTER_NAME, database_name=database,
            collection_name=collection,condition=condition
        )
        #print(collection_data)

        # df_collection_data = pd.DataFrame(list(collection_data))
        # df_collection_data = df_collection_data.drop('_id', axis=1)
        #df_collection_data['Date'] = pd.to_datetime(df_collection_data['Date'])
        #df_collection_data = df_collection_data.set_index('Date')
        #data[collection] = df_collection_data

    return collection_num

#这个是读取数据库订单的，返回的是list形式的数据
# def acquire_from_database():
#     """
#     Acquires all the data (covid data, stock data, technical data, ...)
#     from the MongoDB database.
#
#     Returns:
#         - data (List) : contains all the data of the data acquisition stage
#         in the form of pd.Dataframe(s)
#     """
#     database = costants.DATABASE_NAME
#     data = []
#
#     for collection in costants.COLLECTIONORDER:
#         logging.info(
#             f"\n- Acquiring '{collection}' from the MongoDB '{database}' database")
#         collection_data = read_mongodb_collection(
#             cluster_name=costants.CLUSTER_NAME, database_name=database,
#             collection_name=collection
#         )
#         #print(collection_data)
#         for doc in collection_data:
#             data.append(doc)
#         # df_collection_data = pd.DataFrame(list(collection_data))
#         # df_collection_data = df_collection_data.drop('_id', axis=1)
#         #df_collection_data['Date'] = pd.to_datetime(df_collection_data['Date'])
#         #df_collection_data = df_collection_data.set_index('Date')
#         #data[collection] = df_collection_data
#
#     return data
#




# 如果后面用这个的时候不传输参数projection,加上投影就会出来只显示id的情况不知道是不是默认projection为{}的时候只显示id
def read_mongodb_collection(cluster_name, database_name, collection_name, condition={}):
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

    return collection.find(condition)

def get_record_num(cluster_name, database_name, collection_name, condition={}):
    '''
    Args:
    :return:
    '''
    client = data_storing.connect_cluster_mongodb(
        cluster_name, auth.MONGODB_USERNAME, auth.MONGODB_PASSWORD)
    database = data_storing.connect_database(client, database_name)
    collection = data_storing.connect_collection(database, collection_name)[0]
    return collection.find(condition).count()



def main():
    # start_date = datetime(2017, 4, 1)
    # end_date = datetime(2022, 4, 30)

    # data = download_stock_data(costants.AAPL, start_date, end_date)
    # plt.plot(data)
    # plt.show()
    pass


if __name__ == "__main__":
    main()
