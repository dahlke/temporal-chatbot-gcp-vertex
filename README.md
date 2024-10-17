# AI Chatbot example using GCP Vertex AI

Demonstrates how Temporal and GCP Vertex AI can be used to quickly build bulletproof AI applications.

## Samples

* [basic](basic) - A basic Bedrock workflow to process a single prompt.

## Pre-requisites

1. A GCP account with Vertex AI enabled.
2. A machine that has access to Vertex AI.
3. A local Temporal server running on the same machine. See [Temporal's dev server docs](https://docs.temporal.io/cli#start-dev-server) for more information.

## Running the samples

For these sample, the optional `vertex` dependency group must be included. To include, run:

    poetry install --with vertex

There are 3 Bedrock samples, see the README.md in each sub-directory for instructions on running each.
