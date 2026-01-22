## Notes
- You can use either codespaces or the VScode in the PC

## Docker 101
# 1. docker run -it ubuntu @ Will take you into the docker container check ls
# 2. apt update @ will dependencies etc.
# 3. apt install python3 @ get python
# 4. python3 -V @ Check version #Python 3.12.3


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