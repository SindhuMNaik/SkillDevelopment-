!pip -q install langgraph langchain-groq

import os
from typing import TypedDict
from getpass import getpass
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END

GROQ_API_KEY = getpass("Groq API Key: ")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

class State(TypedDict):
    topic: str
    research: str
    article: str
    review: str

def research_agent(state):
    topic = state["topic"]

    prompt = f"""
You are a Research Agent.

Research the topic:

{topic}

Provide:
1. Simple definition
2. Important concepts
3. Real-world applications
4. Important facts

Explain everything for a beginner.
"""

    response = llm.invoke(prompt)

    return {"research": response.content}

def writer_agent(state):
    research = state["research"]

    prompt = f"""
You are a Writing Agent.

Use the research below to create a beginner-friendly explanation.

RESEARCH:
{research}

Requirements:
- Use simple English
- Use headings
- Give examples
- Keep the explanation easy to understand
"""

    response = llm.invoke(prompt)

    return {"article": response.content}

def reviewer_agent(state):
    article = state["article"]

    prompt = f"""
You are a Review Agent.

Review the following article:

{article}

Check:
1. Is the explanation correct?
2. Is it beginner friendly?
3. Are important points missing?
4. Is anything confusing?

Give a short review and suggestions.
"""

    response = llm.invoke(prompt)

    return {"review": response.content}

graph = StateGraph(State)

graph.add_node("researcher", research_agent)
graph.add_node("writer", writer_agent)
graph.add_node("reviewer", reviewer_agent)

graph.add_edge(START, "researcher")
graph.add_edge("researcher", "writer")
graph.add_edge("writer", "reviewer")
graph.add_edge("reviewer", END)

app = graph.compile()

topic = input("Enter a topic for the AI agents to research: ")

result = app.invoke({
    "topic": topic,
    "research": "",
    "article": "",
    "review": ""
})

print("\nRESEARCH AGENT OUTPUT\n")
print(result["research"])

print("\nWRITER AGENT OUTPUT\n")
print(result["article"])

print("\nREVIEWER AGENT OUTPUT\n")
print(result["review"])

print("\nMULTI-AGENT WORKFLOW COMPLETED")
