#!/bin/bash

echo "Creating job to build index"
srun --nodes=1 --ntasks=1 --mem=16G --cpus-per-task=6 --gres=gpu:1 --partition=gpu --time=00:30:00 --pty \
  singularity exec --nv --no-home ./containers/container-redacted.sif python src/chatbot/build_index.py --data data
