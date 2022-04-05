# Cosmos DB Dummy Data Generator

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