FROM python:3.13.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/ 

WORKDIR /code

COPY pyproject.toml .python-version uv.lock ./
RUN uv sync --locked #Dockerfile installs all Python dependencies specified in your pyproject.toml and uv.lock files using the uv package manager. 


# RUN pip install pandas pyarrow
COPY pipeline.py .
ENTRYPOINT ["uv", "run", "python", "pipeline.py"]
