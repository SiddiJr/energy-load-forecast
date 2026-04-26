FROM nvidia/cuda:12.6.3-cudnn-devel-ubuntu22.04

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip3 install --upgrade pip

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

ENV XLA_FLAGS=--xla_gpu_cuda_data_dir=/usr/local/cuda
ENV LD_LIBRARY_PATH="/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64:${LD_LIBRARY_PATH}"
ENV PATH="/usr/local/cuda/bin:${PATH}"

ENV PYTHONPATH="/app:${PYTHONPATH}"
