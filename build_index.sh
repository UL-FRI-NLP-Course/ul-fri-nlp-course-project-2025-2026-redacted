#!/bin/bash

echo "Converting structured data (CSV/JSON) to text chunks..."
python src/chatbot/convert_structured_data.py

echo ""
echo "Building CPU index..."
srun --nodes=1 --ntasks=1 --mem=16G --cpus-per-task=6 --gres=gpu:1 --partition=gpu --time=00:30:00 --pty \
  singularity exec --nv --no-home ./containers/container-redacted.sif \
  python src/chatbot/build_index.py \
    --data-dir data/reviews_markdown/cpu \
    --extra-dir data/structured_chunks/cpu \
    --output-dir ./rag_index/cpu

echo ""
echo "Building GPU index..."
srun --nodes=1 --ntasks=1 --mem=16G --cpus-per-task=6 --gres=gpu:1 --partition=gpu --time=00:30:00 --pty \
  singularity exec --nv --no-home ./containers/container-redacted.sif \
  python src/chatbot/build_index.py \
    --data-dir data/reviews_markdown/gpu \
    --extra-dir data/structured_chunks/gpu \
    --output-dir ./rag_index/gpu
