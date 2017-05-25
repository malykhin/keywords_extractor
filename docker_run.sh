#!/bin/bash
PORT=3333
docker run -it -p ${PORT}:${PORT} --env EXTRACTOR_PORT=${PORT} keywords-extractor