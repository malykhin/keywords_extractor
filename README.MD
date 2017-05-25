# Keywords, key phrases, named entities extraction API

Based on the textacy, spacy for the NLP operations and Flask for the API

## List of endpoints:
- `/api/keywords` - POST - request body: `{"text": "string", "number": int}`
    response: `{"keywords": [string]}`
- `/api/keyphrases` - POST - request body: `{"text": "string", "number": int}`
    response: `{"keyphrases": [string]}`
- `/api/named_entities` -  POST - request body: `{"text": "string", "number": int}`
    response: `{"named_entities": [string]}`

Don't forget to set `Content-type: application/json` header in the request.

## Installation

- Run `docker_build.sh` to build the Docker container, `docker_run.sh` - for start
- ENV variables `EXTRACTOR_PORT` - app port, default 5000, `EXTRACTOR_DEBUG` - flask debug mode, default false

