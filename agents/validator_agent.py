# agents/validator_agent.py

from .agent_base import AgentBase

class ValidatorAgent(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name="ValidatorAgent", max_retries=max_retries, verbose=verbose)

    def execute(self, topic, article):
        messages = [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You are an AI assistant that validates research articles for accuracy, completeness, and adherence to academic standards."
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Given the topic and the research article below, assess whether the article comprehensively covers the topic, follows a logical structure, and maintains academic standards.\n"
                            "Provide a brief analysis and rate the article on a scale of 1 to 5, where 5 indicates excellent quality.\n\n"
                            f"Topic: {topic}\n\n"
                            f"Article:\n{article}\n\n"
                            "Validation:"
                        )
                    }
                ]
            }
        ]
        validation = self.call_openai(
            messages=messages,
            temperature=0.3,         # Lower temperature for more deterministic output
            max_tokens=500,
            # top_p=1,
            # frequency_penalty=0,
            # presence_penalty=0,
            # response_format={"type": "text"}
        )
        return validation
