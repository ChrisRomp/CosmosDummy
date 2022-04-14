# Sample Kubernetes Files

Examples for k8s files for scaled load testing.

Components:
* Secret: DB URI and key
* Replica Set: Multiple container instances for generating load

Image source: `ghcr.io/chrisromp/cosmosdummy:latest`

## Create the `db-creds` secret

You can create the secret directly in the terminal:

```bash
kubectl create secret generic db-creds \
  --from-literal=uri='https://youraccount.documents.azure.com:443/' \
  --from-literal=key='yourcosmoskey'
```

Or you can use YAML.  First, base64 encode your credentials:

```bash
echo -n 'https://youraccount.documents.azure.com:443/' | base64
echo -n 'yourcosmoskey' | base64
```

Then update the YAML using `secret-db-creds.yaml` as a template with the output from the `base64` encoding:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-creds
type: Opaque
data:
  uri: # base64 encoded Cosmos DB URI
  key: # base64 encoded Cosmos DB key
```

## Create a Deployment

Update the YAML using `deployment-cosmosdummy.yaml` as a template:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cosmosdummy
  labels:
    app: cosmosdummy
spec:
  # Adjust to match load
  replicas: 3
  selector:
    matchLabels:
      app: cosmosdummy
  template:
    metadata:
      labels:
        app: cosmosdummy
    spec:
      containers:
      - name: cosmosdummy-app
        image: ghcr.io/chrisromp/cosmosdummy:latest
        env:
          - name: COSMOS_URI
            valueFrom:
              secretKeyRef:
                name: db-creds
                key: uri
          - name: COSMOS_KEY
            valueFrom:
              secretKeyRef:
                name: db-creds
                key: key
          - name: COSMOS_DB_NAME
            value: db1
          - name: COSMOS_CONTAINER_NAME
            value: orders1
          - name: COSMOS_THROUGHPUT
            value: "400"
          - name: COSMOS_BATCH_SIZE
            value: "2000"
```
