#!/bin/bash
set -e

cd "$(dirname "$0")/.."

echo "Activating environment..."
source venv/bin/activate || conda activate is477

echo "Running Snakemake workflow..."
snakemake -s "Workflow automation and provenance/Snakefile" --cores 1

echo "Workflow complete."
