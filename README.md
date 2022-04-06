# Cosmos DB Dummy Data Generator

Simple app to generate fake data and load to Azure Cosmos DB SQL API using the client library for Python.

## Setting Up

Set the `COSMOS_URI` and `COSMOS_KEY` environment variables:

```bash
export COSMOS_URI="https://[youraccount].documents.azure.com:443/"
export COSMOS_KEY="YourAccountKey"
```

Set the `RUN PARAMS` values in `app/app.py`:

* `DATABASE_NAME` - The Cosmos DB database name
* `CONTAINER_NAME` - The Cosmos DB container name
* `THROUGHPUT` - The offered performance level in RU/s
* `BATCH_SIZE` - The size of each batch before refreshing the context and sample data

## Running the App

```bash
python app/app.py
```

End the loading process with Ctrl+C.

## Data Sample

The format of the generated random data (using [Faker](https://github.com/joke2k/faker)):

```json
{
    "id": "uuid",
    "timestamp": "ISO-8061 current time",
    "name": "string",
    "company": "string",
    "country": "string",
    "orderNumber": int,
    "orderAmount": float(2)
}
```

The app will use `/country` as the partition key by default. This can be modified in `app/client.py`.
