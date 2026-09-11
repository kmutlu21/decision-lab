FROM python:3.14-slim-bookworm
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1
WORKDIR /app
# CPU-only PyTorch matches the verified Windows model runtime.
COPY requirements.txt ./requirements.txt
RUN python -m pip install --no-cache-dir torch==2.14.0+cpu --index-url https://download.pytorch.org/whl/cpu \
    && python -m pip install --no-cache-dir -r requirements.txt
RUN useradd --create-home --uid 10001 appuser
# Explicit source list: research data, credentials and model artifacts are
# provided at runtime, not stored in image layers.
COPY main.py inference.py replay.html objectives.py verify_model.py ./
COPY import_data.py import_functions.py import_model_context.py ./
COPY feature_math.py sql_features.py sql_runtime.py ./
COPY verify_sql_features.py verify_sql_runtime.py bootstrap_database.py ./
USER appuser
EXPOSE 8000
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Read-only competition presentation routes
COPY replay_story.py ./
