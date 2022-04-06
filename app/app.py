'''Sample data loader for Cosmos DB'''
from getsample import generate_sample
from client import get_container
from counter import Counter

# RUN PARAMS
DATABASE_NAME = "db1"
CONTAINER_NAME = "orders1"
THROUGHPUT=400
BATCH_SIZE = 2000

def load_data(count):
    '''Load "X" samples into CosmosDB'''
    samples = generate_sample(count)
    container = get_container(DATABASE_NAME, CONTAINER_NAME, THROUGHPUT)

    print ("Starting batch...")
    for sample in samples:
        counter = Counter.increment()
        print(f"Loading record {counter}...", end="\r")
        container.create_item(sample)

    print ("\nBatch end.")

print("Staring...")
while True:
    try:
        load_data(BATCH_SIZE)
    except KeyboardInterrupt:
        print("\nStopping load...")
        break

print("Done.")
