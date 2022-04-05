'''Generate Cosmos DB client'''
import os
from azure.cosmos import CosmosClient, PartitionKey

URL = os.environ['COSMOS_URI']
KEY = os.environ['COSMOS_KEY']
client = CosmosClient(URL, credential=KEY)

def get_container(database_name, container_name, throughput):
    '''Get Cosmos DB container'''
    print("Connecting to Cosmos DB...")

    database = client.create_database_if_not_exists(database_name)

    container = database.create_container_if_not_exists(
        id=container_name,
        partition_key=PartitionKey(path="/country"),
        offer_throughput=throughput
    )

    return container
