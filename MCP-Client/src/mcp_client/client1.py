import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from langchain_core.messages import toolMessage

load_dotenv()

SERVER = {
    "math": {
        "transport" : "stdio",
        "command" : "/snap/bin/uv",
        "args" : [
            "run",
            "fastmcp",
            "run",
            "/home/raza/Programming/MCP-Server/Local-MCP-Server-for_Math/src/local_mcp_server_for_math/main.py"
        ]
    }
}

async def main():
    client = MultiServerMCPClient(SERVER)
    tools = await client.get_tools()

    named_tool = {}
    for tool in tools:
        named_tool[tool.name] = tool


    llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    max_tokens=1000 
    )
    llm_with_tools = llm.bind_tools(tools)

    prompt = "What is the product of 2 and 12?"
    response = await llm_with_tools.ainvoke(prompt)

    if not getattr(response, "tool_calls", None):
        print("No tool calls were made.")
        return

    selected_tool = response.tool_calls[0]["name"]
    selected_tool_args = response.tool_calls[0]["args"]
    selected_tool_id = response.tool_calls[0]["id"]

    tool_result = await named_tool[selected_tool].ainvoke(selected_tool_args)

    tool_message = toolMessage(
        content=tool_result,
        tool_call_id = selected_tool_id
        )

    final_response = await llm_with_tools.ainvoke(prompt, response, tool_message)


if __name__ == "__main__":
    asyncio.run(main())




