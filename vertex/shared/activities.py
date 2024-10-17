import json

from temporalio import activity


class VertexActivities:
    def __init__(self) -> None:
        self.vertex = None

    @activity.defn
    def prompt_vertex(self, prompt: str) -> str:
        """
        # Model params
        modelId = "meta.llama2-70b-chat-v1"
        accept = "application/json"
        contentType = "application/json"
        max_gen_len = 512
        temperature = 0.1
        top_p = 0.2

        body = json.dumps(
            {
                "prompt": prompt,
                "max_gen_len": max_gen_len,
                "temperature": temperature,
                "top_p": top_p,
            }
        )

        response = self.vertex.invoke_model(
            body=body, modelId=modelId, accept=accept, contentType=contentType
        )

        response_body = json.loads(response.get("body").read())

        return response_body.get("generation")
        """

        return "GCP vertex response", self.vertex
