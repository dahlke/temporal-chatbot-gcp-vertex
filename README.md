# AI Chatbot example using GCP Vertex AI

Demonstrates how Temporal and GCP Vertex AI can be used to quickly build bulletproof AI applications.

## Samples

* [basic](basic) - A basic Bedrock workflow to process a single prompt.

## Pre-requisites

1. A GCP account with Vertex AI enabled.
2. A machine that has access to Vertex AI.
3. A local Temporal server running on the same machine. See [Temporal's dev server docs](https://docs.temporal.io/cli#start-dev-server) for more information.

## Running the samples

First, you'll need to provide your GCP credentials as well as the project ID that you'll be working in.

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/Users/neildahlke/.gcp/rick-1-389616-0b290d9dcbe3.json"
export PROJECT_ID="foo-1-111111"
```

Then, install the dependencies.

```bash
poetry install
```

Once the dependencies have been run, start the worker.

```bash
poetry run python run_worker.py
```

With the worker running, send a prompt.

```bash
poetry run python send_message.py "what is the capital of france?"
```
