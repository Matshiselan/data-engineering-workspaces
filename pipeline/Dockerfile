FROM python:3.13.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/ 

WORKDIR /code

COPY pyproject.toml .python-version uv.lock ./
RUN uv sync --locked #Dockerfile installs all Python dependencies specified in your pyproject.toml and uv.lock files using the uv package manager. 

COPY ingest_data.py .

# RUN pip install pandas pyarrow
COPY pipeline.py .
COPY load_green_and_zones.py .
# Copy green trip data and taxi_zone_lookup.csv if present
COPY green_tripdata* .
COPY taxi_zone_lookup.csv .

# Add entrypoint script to run both scripts
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
