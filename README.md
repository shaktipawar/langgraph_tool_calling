# langgraph_tool_calling
This application helps in understanding how Tool calling works in Custom Agent Graph workflow.

![alt text](image.png)

# Prerequisites
* Create vitual environment on your system (for Windows).
Be inside project root folder (langgraph_tool_calling)
    ```
    python -m venv venv
    cd venv
    cd scripts
    activate
    cd..
    cd..

    pip install -r requirements.txt
    ```
* Inside project root folder (langgraph_tool_calling), create config.yaml and update following values.
    ```
    OPENAI_API_KEY: "<<ADD YOUR OPEN_AI_KEY>>"
    LANGCHAIN_TRACING_V2 : "true"
    LANGCHAIN_ENDPOINT : "https://api.smith.langchain.com"
    LANGCHAIN_API_KEY : "<<ADD YOUR LANGSMITH API KEY>>"
    LANGCHAIN_PROJECT : "<<ADD YOU LANGSMITH FOLDER>>"

    ```
<br>
<br>