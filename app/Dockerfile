
FROM python:3.9
COPY app.py /app.py
RUN pip install flask opentelemetry-distro[otlp] opentelemetry-instrumentation opentelemetry-instrumentation-flask
CMD opentelemetry-instrument python app.py
