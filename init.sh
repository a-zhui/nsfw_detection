#!/bin/bash
source /root/miniconda3/bin/activate nsfw_detection
uvicorn --host 0.0.0.0 --port 7860 main:app