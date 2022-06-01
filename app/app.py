'''Sample data loader for Cosmos DB'''
import os
from getsample import generate_sample
from client import get_container
from counter import Counter
from dotenv import load_dotenv
load_dotenv()

# RUN PARAMS
DATABASE_NAME = os.environ["COSMOS_DB_NAME"]
CONTAINER_NAME = os.environ["COSMOS_CONTAINER_NAME"]
THROUGHPUT = int(os.getenv("COSMOS_THROUGHPUT", default="400"))
BATCH_SIZE = int(os.getenv("COSMOS_BATCH_SIZE", default="2000"))

def load_data(count):
    '''Load "X" samples into CosmosDB'''
    samples = generate_sample(count)
    container = get_container(DATABASE_NAME, CONTAINER_NAME, THROUGHPUT)

    print ("Starting batch...")
    for sample in samples:
        counter = Counter.increment()
        print(f"Loading record {counter}...", end="\r")
        container.create_item(sample)
        container.query_items(query='select * from c where c.country ="Afghanistan" ',enable_cross_partition_query=True)


    print ("\nBatch end.")

print("Staring...")
while True:
    try:
        load_data(BATCH_SIZE)
    except KeyboardInterrupt:
        print("\nStopping load...")
        break

print("Done.")
