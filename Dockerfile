FROM python:3.11.1-buster@sha256:229b45f2c25a02f9307031eca88067f33613ada05a3fb8ee24115bb8eb903459 as build

RUN apt-get update
RUN apt-get install -y  --no-install-recommends \
    build-essential gcc

RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt


FROM python:3.11.1-buster@sha256:229b45f2c25a02f9307031eca88067f33613ada05a3fb8ee24115bb8eb903459

RUN groupadd python && \
    useradd -r -g python usr
RUN mkdir /usr/app && chown usr:python /usr/app
WORKDIR /usr/app

COPY --chown=usr:python --from=build /usr/app/venv /usr/app/venv
COPY --chown=usr:python . .

USER usr:python

ENV PATH="/usr/app/venv/bin:$PATH"
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi"]
HEALTHCHECK --interval=30s --timeout=30s --start-period=15s --retries=3 CMD curl -f http://localhost:8000/health
