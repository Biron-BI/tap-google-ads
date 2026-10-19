FROM python:3.13-slim

COPY . tap-google-ads/

RUN cd tap-google-ads

WORKDIR tap-google-ads

RUN pip install -e .

# Your application run command
ENTRYPOINT ["tap-google-ads"]
