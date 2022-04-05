'''Sample Data Helper'''
import datetime
import uuid
from faker import Faker

fake = Faker()

def generate_sample(count):
    '''Get next "X" samples'''
    print(f"Generating {count} samples...")

    data = []
    for _ in range(count):
        data.append({
            "id": str(uuid.uuid4()),
            "timestamp": datetime.datetime.now().isoformat(),
            "name": fake.name(),
            "company": fake.company(),
            "country": fake.country(),
            "orderNumber": fake.pyint(),
            "orderAmount": fake.pyfloat(left_digits=2, right_digits=2, positive=True)
        })

    return data
