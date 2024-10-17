# AI Chatbot example using GCP Vertex AI

Demonstrates how Temporal and GCP Vertex AI can be used to quickly build bulletproof AI applications.

## Samples

* [basic](basic) - A basic Bedrock workflow to process a single prompt.
* [signals_and_queries](signals_and_queries) - Extension to the basic workflow to allow multiple prompts through signals & queries.
* [entity](entity) - Full multi-Turn chat using an entity workflow..

## Pre-requisites

1. A GCP account with Vertex AI enabled.
2. A machine that has access to Vertex AI.
3. A local Temporal server running on the same machine. See [Temporal's dev server docs](https://docs.temporal.io/cli#start-dev-server) for more information.

These examples use Amazon's Python SDK (Boto3). To configure Boto3 to use your AWS credentials, follow the instructions in [the Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html).

## Running the samples

For these sample, the optional `vertex` dependency group must be included. To include, run:

    poetry install --with vertex

There are 3 Bedrock samples, see the README.md in each sub-directory for instructions on running each.


# TODO

- clean up AWS mentions and README

```bash
poetry install --with google-cloud-aiplatform
```

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/keyfile.json"
```