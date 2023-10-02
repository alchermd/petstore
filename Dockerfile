FROM python:3.11.5-slim@sha256:a28fdf3bde6c0c97b656841669f6b4cc8164d0f34067c6ce6b5532effe94f8a7 as build

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y  --no-install-recommends build-essential gcc

RUN python -m venv /usr/venv
ENV PATH="/usr/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt


FROM python:3.11.5-slim@sha256:a28fdf3bde6c0c97b656841669f6b4cc8164d0f34067c6ce6b5532effe94f8a7

RUN apt-get update && \
    apt-get install -y  --no-install-recommends curl

RUN groupadd python && \
    useradd -r -g python usr && \
    mkdir /usr/app && \
    chown usr:python /usr/app && \
    mkdir /usr/venv && \
    chown usr:python /usr/venv
WORKDIR /usr/app

COPY --chown=usr:python --from=build /usr/venv /usr/venv
COPY --chown=usr:python . .

USER usr:python

ENV PATH="/usr/venv/bin:$PATH"
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi"]
HEALTHCHECK --interval=30s --timeout=30s --start-period=15s --retries=3 CMD curl -f http://localhost:8000/health
