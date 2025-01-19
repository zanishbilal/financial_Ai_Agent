from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo


web_search_agent=Agent(
    
    name="web search agent",
    role="search the web for information",
    Model=Groq("llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["always include resources"],
    show_tool_calls=True,
    markdown=True,

)


financial_agent=Agent(
    name="finance agent",
    Model=Groq("llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=["use the tables to display the data"],
    show_tool_calls=True,
    markdown=True,
 
    
)

muilti_ai_agent=Agent(
    team=[web_search_agent,financial_agent],
    instructions=["always include sources","use tables to display data"],
    show_tool_calls=True,
    markdown=True,
 
)

muilti_ai_agent.print_response("summarize analyst recommendation and share the latest news for nvidea ",stream=True)