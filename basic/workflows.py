from datetime import timedelta

from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from shared.activities import VertexActivities

@workflow.defn
class BasicVertexWorkflow:
    @workflow.run
    async def run(self, prompt: str) -> str:

        workflow.logger.info("Prompt: %s" % prompt)
        print("Prompt: %s" % prompt)

        response = await workflow.execute_activity_method(
            VertexActivities.prompt_vertex,
            prompt,
            schedule_to_close_timeout=timedelta(seconds=100),
        )

        workflow.logger.info("Response: %s" % response)

        return response


