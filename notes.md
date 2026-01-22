## Notes
- You can use either codespaces or the VScode in the PC

## Docker 101
1. docker run -it ubuntu @ Will take you into the docker container check ls
2. apt update @ will dependencies etc.
3. apt install python3 @ get python
4. python3 -V @ Check version #Python 3.12.3


# Running PostgreSQL with Docker
```
mkdir ny_taxi_postgres_data
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql \
  -p 5432:5432 \
  postgres:18
```
uv add --dev pgcli
uv run pgcli -h localhost -p 5432 -u root -d ny_taxi

# Command Line Interface (CLI)

```
uv run python ingest_data.py \
  --pg_user=root \
  --pg_pass=root \
  --pg_host=localhost \
  --pg_port=5432 \
  --pg_db=ny_taxi \
  --year=2021 \
  --month=1
```

in docker we would 

```
docker run -it --rm \
  taxi_ingest:v001 \
    --pg_user=root \
    --pg_pass=root \
    --pg_host=localhost \
    --pg_port=5432 \
    --pg_db=ny_taxi \
    --year=2021 \
    --month=1
```


## Network

```
docker network create pg-network

docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v ny_taxi_postgres_data:/var/lib/postgresql \
  -p 5432:5432 \
  --network=pg-network \
  --name pgdatabase \
  postgres:18
```

```
# In another terminal, run pgAdmin on the same network
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -v pgadmin_data:/var/lib/pgadmin \
  -p 8085:80 \
  --network=pg-network \
  --name pgadmin \
  dpage/pgadmin4
```

## Loading data to docker network

```
docker run -it --rm \
  --network=pipeline_pg-network \
  taxi_ingest:v001 \
    --pg_user=root \
    --pg_pass=root \
    --pg_host=pgdatabase \
    --pg_port=5432 \
    --pg_db=ny_taxi \
    --year=2021 \
    --month=1
```