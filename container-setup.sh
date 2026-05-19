#!/bin/bash

echo "Creating container!"
singularity build ./containers/container-redacted.sif docker://nvcr.io/nvidia/pytorch:24.12-py3
echo "Installing additional packages"
singularity exec ./containers/container-redacted.sif pip install "transformers==4.47.0" "sentence-transformers==3.3.1" "accelerate==1.2.1" "faiss-cpu>=1.7.4" "numpy>=1.24" accelerate --upgrade
