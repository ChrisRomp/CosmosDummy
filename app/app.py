'''Sample data loader for Cosmos DB'''
from getsample import generate_sample
from client import get_container

# RUN PARAMS
DATABASE_NAME = "db1"
CONTAINER_NAME = "orders1"
THROUGHPUT=400
BATCH_SIZE = 2000

COUNTER = 0

def load_data(count):
    '''Load "X" samples into CosmosDB'''
    samples = generate_sample(count)
    container = get_container(DATABASE_NAME, CONTAINER_NAME, THROUGHPUT)

    print ("Starting batch...")
    for sample in samples:
        global COUNTER
        print(f"Loading record {format(COUNTER)}...", end="\r")
        container.create_item(sample)
        COUNTER += 1

    print ("Batch end.")

print("Staring...")
while True:
    try:
        load_data(BATCH_SIZE)
    except KeyboardInterrupt:
        print("\nStopping load...")
        break

print("Done.")
