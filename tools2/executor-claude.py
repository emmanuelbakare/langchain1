import os
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_anthropic import ChatAnthropic
from langchain.memory import ConversationBufferMemory
from langchain.tools import Tool
from dotenv import load_dotenv

# Load environment variables

load_dotenv()


class CodeGenerationAgent:
    def __init__(self):
        # Initialize memory
        self.memory = ConversationBufferMemory(
            memory_key="chat_history", 
            return_messages=True
        )
        
        # System message for code generation
        self.system_message = """
        You are an expert code generation assistant. 
        Your task is to generate Python code and store it in a Python file.
        Key guidelines:
        - Generate clean, efficient, and well-documented code
        - If no filename is specified, use "generated_code.py" as the default
        - Ensure the code is functional and follows best practices
        - Handle potential edge cases and include necessary imports
        """
        
        # Initialize Claude model
        self.llm = ChatAnthropic(
                    anthropic_api_key=os.getenv("CLAUDE_API_KEY"),
                    model_name = "claude-3-5-sonnet-20240620"
                    )
        
        # Prompt template
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", self.system_message),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{code_request}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])
    
    def create_code_writer_tool(self):
        """
        Create a tool to write code to a file
        
        Args:
            code (str): The code to be written
            filename (str, optional): Name of the file to write code to
        
        Returns:
            bool: True if file was written successfully, False otherwise
        """
        def code_writer(code, filename="generated_code.py"):
            try:
                with open(filename, 'w') as f:
                    f.write(code)
                return f"Code successfully written to {filename}"
            except Exception as e:
                return f"Error writing code: {str(e)}"
        
        return Tool(
            name="code_writer",
            func=code_writer,
            description="Write generated code to a Python file"
        )
    
    def setup_agent(self):
        """
        Set up the agent with tools and prompt template
        
        Returns:
            AgentExecutor: Configured agent executor
        """
        # Create tools
        tools = [self.create_code_writer_tool()]
        
        # Create agent
        agent = create_tool_calling_agent(
            llm=self.llm, 
            prompt=self.prompt_template,
            tools=tools
        )
        
        # Create executor
        executor = AgentExecutor(
            agent=agent,
            tools=tools,
            verbose=True,
            memory=self.memory
        )
        
        return executor
    
    def generate_code(self, code_request):
        """
        Generate code based on user request
        
        Args:
            code_request (str): Description of code to generate
        
        Returns:
            dict: Result of code generation
        """
        # Setup the agent
        executor = self.setup_agent()
        
        try:
            # Invoke the agent with the code request
            result = executor.invoke({"code_request": code_request})
            
            # Print and return the output
            print("Generated Code Result:")
            print(result.get('output', 'No output generated'))
            
            return result
        
        except Exception as e:
            print(f"An error occurred during code generation: {e}")
            return {"error": str(e)}
    
    def interactive_code_generation(self):
        """
        Interactive code generation interface
        """
        print("Claude Code Generation Assistant")
        print("--------------------------------")
        
        while True:
            # Get user input
            code_request = input("\nEnter your code generation request (or 'quit' to exit): ")
            
            # Check for exit condition
            if code_request.lower() in ['quit', 'exit', 'q']:
                print("Exiting code generation assistant.")
                break
            
            # Generate code
            self.generate_code(code_request)

def main():
    # Create and run the code generation agent
    agent = CodeGenerationAgent()
    agent.interactive_code_generation()

if __name__ == "__main__":
    main()