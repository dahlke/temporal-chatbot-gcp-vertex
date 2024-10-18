import os
import vertexai
from temporalio import activity
from vertexai.generative_models import GenerativeModel, GenerationConfig

PROJECT_ID = os.environ.get("PROJECT_ID")
REGION = os.environ.get("REGION", "us-central1")

class VertexActivities:
    def __init__(self) -> None:
        self.vertex = None

    @activity.defn
    def prompt_vertex(self, prompt: str) -> str:
        vertexai.init(project=PROJECT_ID, location=REGION)

        model = GenerativeModel("gemini-1.5-flash-002")

        response = model.generate_content(
            prompt,
            generation_config=GenerationConfig(
                    temperature=0.1,
                    # top_p=0.95,
                    # top_k=20,
                    top_p=0.2,
                    candidate_count=1,
                    max_output_tokens=512,
                    seed=5,
                )
        )

        return response.text
