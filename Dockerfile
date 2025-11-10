FROM python:3.11-slim
WORKDIR /work
COPY . .
RUN pip install pandas
ENTRYPOINT [ "python", "src/compute_latency.py" ]
