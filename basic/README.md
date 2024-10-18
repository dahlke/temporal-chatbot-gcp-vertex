# Basic GCP Vertex AI workflow

A basic Vertex AI workflow. Starts a workflow with a prompt, generates a response and ends the workflow.

To run, first see `samples-python` [README.md](../../README.md), and `vertex` [README.md](../README.md) for prerequisites specific to this sample. Once set up, run the following from this directory:

1. Run the worker: `poetry run python run_worker.py`
2. In another terminal run the client with a prompt:

    e.g. `poetry run python send_message.py 'What animals are marsupials?'`