"""Script to collect input LLM prompts.

It outputs responses in Label Studio project.
"""
from langchain_community.callbacks.labelstudio_callback import (
    LabelStudioCallbackHandler,
)
from langchain_openai import OpenAI

project_name = "LLM Eval Annotator"

llm = OpenAI(
    temperature=0, callbacks=[LabelStudioCallbackHandler(project_name=project_name)]
)

print(llm("Tell me a joke"))
