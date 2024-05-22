# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12.3
FROM python:${PYTHON_VERSION}-slim AS base

# Set python environments
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
RUN --mount=type=bind,source=Pipfile,target=Pipfile \
    --mount=type=bind,source=Pipfile.lock,target=Pipfile.lock \
    pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --ignore-pipfile --dev --system &&\
    useradd -r -M -s /usr/sbin/nologin appuser

# Copy the source code into the container.
COPY . .

# Expose the port that the application listens on.
EXPOSE 8000

# Switch to the non-privileged user to run the application.
USER appuser

# Run the application.
CMD ["gunicorn", \
    "-w", "1", \
    "--reload", \
    "-b", "0.0.0.0:8000", \
    "src.wsgi:application"]
