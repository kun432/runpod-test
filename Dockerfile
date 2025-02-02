FROM python:3.10-slim

WORKDIR /
RUN pip install --no-cache-dir runpod
COPY rp_handler.py /

# コンテナを起動
CMD ["python3", "-u", "rp_handler.py"]