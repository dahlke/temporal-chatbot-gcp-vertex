import asyncio
import sys

from temporalio.client import Client
from workflows import BasicVertexWorkflow


async def main(prompt: str) -> str:
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Start the workflow
    workflow_id = "basic-vertex-workflow"
    handle = await client.start_workflow(
        BasicVertexWorkflow.run,
        prompt,  # Initial prompt
        id=workflow_id,
        task_queue="vertex-task-queue",
    )
    return await handle.result()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python send_message.py '<prompt>'")
        print("Example: python send_message.py 'What animals are marsupials?'")
    else:
        result = asyncio.run(main(sys.argv[1]))
        print(result)
