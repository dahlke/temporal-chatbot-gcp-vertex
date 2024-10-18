# AI Chatbot example using GCP Vertex AI

Demonstrates how Temporal and GCP Vertex AI can be used to quickly build bulletproof AI applications.

## Samples

* [basic](basic) - A basic Vertex AI workflow to process a single prompt.
* [signals_and_queries](signals_and_queries) - Extension to the basic workflow to allow multiple prompts through signals & queries.
* [entity](entity) - Full multi-Turn chat using an entity workflow..


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
