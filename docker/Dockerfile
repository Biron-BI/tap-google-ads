FROM python:3.10-slim

COPY . tap-google-ads/

RUN cd tap-google-ads

WORKDIR tap-google-ads

RUN pip install -e .

# Your application run command
ENTRYPOINT ["tap-google-ads"]
