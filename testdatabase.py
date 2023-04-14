import sys
import ssl
# from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import time

import logging

# import mqtt_comm


import data_storing, costants, data_acquisition,data_delete,auth


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
    )

    """
    Turns on the back end of the project
    """
    client_id = "back-end"
    endpoint = "a1o1h9paav6wpy-ats.iot.eu-west-2.amazonaws.com"
    port = 8883
    CA_path = "./certificates/AmazonRootCA1.pem"
    privateKey_path = "./certificates/privateKey.pem"
    certificate_path = "./certificates/certificate.pem"
    incoming_topic = "arduino/outgoing"
    outgoing_topic = "backend/outgoing"

    # client = mqtt_comm.configure_client(client_id=client_id,
    #                                     endpoint=endpoint,
    #                                     port=port,
    #                                     CA_path=CA_path,
    #                                     privateKey_path=privateKey_path,
    #                                     certificate_path=certificate_path)

    # mqtt_comm.connect_client(client=client)

    # mqtt_comm.subscribe_to_topic(client=client,
    #                             topic=incoming_topic,
    #                             callback_function=mqtt_comm.print_incoming_message)

    # message = "HELLO GUYS !!!!!"
    # mqtt_comm.publish_on_topic(client=client,
    #                           topic=outgoing_topic,
    #                           message=message)

    # 假数据
    # data_dict = {'name': 'chocolate', 'code': '3', 'price': '3'}
    # data_storing.store_dict_into_mongodb(costants.CLUSTER_NAME, costants.DATABASE_NAME, costants.COLLECTION_MESSAGE,data_dict)

    # data = data_acquisition.get_from_products()
    # print(data)
    # data = data_acquisition.get_from_products(conditionproduct={'code': '3'})
    # print(data[0])
    # data=data[0]
    # print(data['code'])
    # data_delete.delete_mongodb_collection()
    # data_delete.delete_one_record(condition={'nikename':'mike'})
    database = costants.DATABASE_NAME
    cluster_name = costants.CLUSTER_NAME
    database_name = database
    collection_name = costants.COLLECTION_MESSAGE
    client = data_storing.connect_cluster_mongodb(
        cluster_name, auth.MONGODB_USERNAME, auth.MONGODB_PASSWORD)
    database = data_storing.connect_database(client, database_name)
    collection = data_storing.connect_collection(database, collection_name)[0]
    # logging.info(
    #     f"\n- Reading the '{collection_name}' collection in the '{database_name}' database")
    collection.update_one({'id': '1'},
                          {'$set': {"nikename": '123', "info": '123', "date": '123'}})
if __name__ == "__main__":
    main()

# client = AWSIoTMQTTClient('back-end')
# client.configureEndpoint('a1o1h9paav6wpy-ats.iot.eu-west-2.amazonaws.com', 8883)
# client.configureCredentials("./certificates/AmazonRootCA1.pem","./certificates/privateKey.pem","./certificates/certificate.pem")


# client.configureAutoReconnectBackoffTime(1, 32, 20)
# client.configureOfflinePublishQueueing(-1)
# client.configureDrainingFrequency(2)
# client.configureConnectDisconnectTimeout(10)
# client.configureMQTTOperationTimeout(5)
# client.connect()
# print("Client Connected")

