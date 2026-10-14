import asyncio
import os
import sys

from dotenv import load_dotenv

from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage

load_dotenv()

async def main():
    async for message in query(
        prompt="Review utils.py for bugs that would cause crashes. Fix any issues you find.",
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Edit", "Glob"],  # これらのツールを自動承認します
            permission_mode="acceptEdits",  # ファイル編集を自動承認します
        ),
    ):

        if isinstance(message, AssistantMessage):
            for block in message.content:
                if hasattr(block, "text"):
                    print(block.text)
                elif hasattr(block,"name"):
                    print(f"Tool: {block.name}")
        elif isinstance(message, ResultMessage):
            print(f"Done: {message.subtype}")                

asyncio.run(main())
