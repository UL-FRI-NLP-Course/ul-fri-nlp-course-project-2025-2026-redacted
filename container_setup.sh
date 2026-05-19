#!/bin/bash

mkdir containers
echo "Creating container!"
singularity build ./containers/container-redacted.sif container.def
