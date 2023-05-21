from langchain import LLMMathChain
from langchain.tools import ShellTool
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from ham_egg_convert_tool import HamEggConvertTool
import os


llm = OpenAI(temperature=0)

shell_tool = ShellTool()
llm_math_chain = LLMMathChain(llm=llm, verbose=True)
ham_egg_convert_tool = HamEggConvertTool()

tools = [
    Tool(
        name = "shell",
        func=shell_tool.run,
        description="Linuxコマンドを実行する場合に利用することができます｡"
    ),
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="計算をする場合に利用することができます。"
    ),
    Tool(
        name="Ham Egg Convert",
        func=ham_egg_convert_tool.run,
        description="hamという単語が見つかればeggに置換することができます｡"
    )
]
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

agent.run("'今日のhamとeggはおいしいな｡'という文章を置換後に出現するeggの数を教えてください")
