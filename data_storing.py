"""
This module contains the functions to store data both locally and
remotely into a MongoDB database
"""

import logging
import os

#import pandas as pd
import pymongo
import auth, costants



# def data_storing(data, raw):
#     """
#     Performs the data storing phase of the project

#     Args:
#         - data (Dict): Contains the data that we want to store
#         - raw (bool): indicates if the data to store is acquired
#         raw data or cleaned and prepared data

#     Returns: None
#     """
#     #data_copy = data.copy()
#     logging_utilities.print_name_stage_project("DATA STORING")

#     if not os.path.exists(costants.DATA_FOLDER):
#         os.mkdir(costants.DATA_FOLDER)

#     if raw:
#         database_name = costants.DATABASE_NAME_RAW
#         file_folder = "raw"
#     else:
#         database_name = costants.DATABASE_NAME_PREPARED
#         file_folder = "prepared"

#     file_folder = os.path.join(costants.DATA_FOLDER, file_folder)
#     if not os.path.exists(file_folder):
#         os.mkdir(file_folder)

#     for data_name, data_value in data.items():
#         data_value_copy = data_value.copy()
#         # Storing locally
#         file_name = costants.LOCAL_STORING_FILE_NAMES[data_name]
#         file_path = os.path.join(file_folder, file_name)
#         data_value_copy.to_csv(file_path, sep=costants.SEPARATOR, na_rep="NaN")
#         logging.info(f"\n- STORED '{data_name}' LOCALLY IN {file_path}")

#         # Storing remotely
#         # Note: if the data already exists in the database the remote storing
#         # is not going to be performed, to not duplicate the data
#         store_df_into_mongodb(
#             cluster_name=costants.CLUSTER_NAME, database_name=database_name,
#             collection_name=data_name, df=data_value_copy
#         )


def store_dict_into_mongodb(cluster_name, database_name, collection_name, data_dict):
    """
    Inserts a pandas dataframe into a MongoDb database in the form of a collection

    Args:
        - cluster_name (str): Name of the cluster
        - database_name (str): Name of the database
        - collection_name (str): Name of the collection
        - df (pandas.core.frame.DataFrame): dataframe we want to insert into the
        database as a collection

    Returns: None
    """
    # if 'Date' in df.columns:
    #     # we convert th 'Date' column into string type because pymongo returns
    #     # an error with the datetime.date type
    #     df['Date'] = df['Date'].astype(str)

    # if there is not 'Date' but another index column with datetime type
    # create the column 'Date' of string type (see why string type in the
    # comment above) and set it as the index column
    # elif type(df.index) == pd.core.indexes.datetimes.DatetimeIndex:
    #     df['Date'] = df.index.astype(str)

    #df_dict = df.to_dict(orient='records')
    data_dict = [data_dict]
    store_collection_into_db(
        cluster_name=cluster_name, database_name=database_name, collection_name=collection_name, data=data_dict
    )


def store_collection_into_db(
    cluster_name, database_name, collection_name, data
):
    """
    Inserts a list of MongoDB documents (dictionaries) into a specific collection of a database of a cluster.

    Args:
        - cluster_name (str): Name of the cluster
        - database_name (str): Name of the database
        - collection_name (str): Name of the collection
        - data (List): List of dictionaries, where every dictionary represents a row (document) in the collection

    Returns:
        - None
    """
    client = connect_cluster_mongodb(
        cluster_name, auth.MONGODB_USERNAME, auth.MONGODB_PASSWORD
    )
    database = connect_database(client, database_name)
    collection, collection_already_exists = connect_collection(
        database, collection_name)

    # if collection_already_exists:
    #     logging.info(
    #         f"- ATTENTION: Because the collection '{collection_name}' you are trying to insert into the '{database_name}' database already exists, the insertion is not going to be performed to not duplicate the data")
    # else:
    print(data)
    collection.insert_many(data)
    logging.info(
        f"- STORED '{collection_name}' REMOTELY IN THE {database_name} DATABASE")


def connect_cluster_mongodb(cluster_name, username, password):
    """
    Opens a connection with a MongoDB cluster

    Args:
        - cluster_name (str): name of the cluster
        - username (str): username used ofr authentication
        - password (str): password used for authentication

    Returns:
        - client (MongoClient): client we use to comunicate with the database
    """
    #connection_string = f"mongodb+srv://{username}:{password}@{cluster_name}.bhcapcy.mongodb.net/?retryWrites=true&w=majority"
    connection_string = f"mongodb://{username}:{password}@ac-sh3a7ys-shard-00-00.rjmwtmn.mongodb.net:27017,ac-sh3a7ys-shard-00-01.rjmwtmn.mongodb.net:27017,ac-sh3a7ys-shard-00-02.rjmwtmn.mongodb.net:27017/?ssl=true&replicaSet=atlas-n4ij5c-shard-0&authSource=admin&retryWrites=true&w=majority"
    #mongodb://<username>:<password>@ac-sh3a7ys-shard-00-00.rjmwtmn.mongodb.net:27017,ac-sh3a7ys-shard-00-01.rjmwtmn.mongodb.net:27017,ac-sh3a7ys-shard-00-02.rjmwtmn.mongodb.net:27017/?ssl=true&replicaSet=atlas-n4ij5c-shard-0&authSource=admin&retryWrites=true&w=majority
    # print(connection_string)
    client = pymongo.MongoClient(connection_string)
    # logging.info(f"\n- Connected to '{cluster_name}' MongoDB cluster.")

    return client


def connect_database(client, database_name):
    """
    Returns a specific database of a MongoDB cluster

    Args:
        - client (MongoClient): client object
        - database_name (str): name of the databse we want to connect to

    Returns:
        - database (MongoDatabase): database object
    """
    # If databse doen't exist in the cluster it creates automatically
    if database_name not in client.list_database_names():
        logging.info(
            f"- The '{database_name}' database doesn't exist so MongoDB is going to create it automatically."
        )
    database = client[database_name]

    return database


def connect_collection(database, collection_name):
    """
    Returns a specific collection of a MongoDB database

    Args:
        - database (pymongo.database.Database): database object
        - collection_name (str): name of the collection we want to connect to

    Returns:
        - collection (pymongo.collection.Collection): collection object
        - collection_already_exists (bool): indicates if the collection already
        existed into the database
    """
    collection_already_exists = False
    # If collection doesn't exist in the database it creates automatically
    if collection_name not in database.list_collection_names():
        logging.info(
            f"- The '{collection_name}' collection doesn't exist in the {database.name} database so MongoDB is going to create it automatically."
        )
    else:
        collection_already_exists = True

    collection = database[collection_name]

    return collection, collection_already_exists


def main():
    # cluster = "daps2022"
    # database = "hackathon_DAPS"
    # collection = "google_jax_commits"

    pass


if __name__ == "__main__":
    main()
