# Cosmos DB Dummy Data Generator

Simple app to generate fake data and load to Azure Cosmos DB using the client library for Python.

## Setting Up

Copy the `.env.sample` file to `.env` and set the parameters in `.env`.

```bash
cp .env.sample .env
```

### Parameters

| Parameter | Required | Default | Note |
| --------- | -------- | ------- | ---- |
| `COSMOS_URI` | Yes | None | The URI for your Cosmos DB instance |
| `COSMOS_KEY` | Yes | None | A valid read-write key for your Cosmos DB instance |
| `COSMOS_DB_NAME` | Yes | None | The Cosmos DB database name|
| `COSMOS_CONTAINER_NAME` | Yes | None | The Cosmos DB container name|
| `COSMOS_THROUGHPUT` | No | 400 | The offered performance level in RU/s|
| `COSMOS_BATCH_SIZE` | No | 2000 | The size of each batch before refreshing the |
| `SAMPLE_COUNTRY` | No | None | If set, all sample data will use this static Country value

If you wish to generate load against a single partition key, `/Country`, you can set the `SAMPLE_COUNTRY` parameter and the data will use that value for the `Country` property on all of the generated samples.

## Running the App

```bash
python app/app.py
```

End the loading process with Ctrl+C.

## Scaling Out

Azure Kubernetes Service (AKS) or any k8s implementation can be used to scale out this app and generate additional load. See the [kubernetes](kubernetes) folder for details.

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

The sample data format can be modified in `app/getsample.py`.

The app will use `/country` as the partition key by default. This can be modified in `app/client.py`.
