# Description: Main file to run the code
from llm_integration.llm_handler import LLM_Handler
from utils.parser import Parser

def main():
    # Example usage
    llm_handler = LLM_Handler("llama3.1")
    parser = Parser()
    commands = ["pickup", "putdown"]
    viable_objects = ["red apple", "green apple"]
    instructions = f"Return a list of Commands [{commands}] and their respective objects [] in JSON format for the following statements:"
    
    input = "Pick up the red apple, Put down the red apple, Pick up the green apple, throw the green apple, put the green apple down"
    
    result = llm_handler.predict(instructions + "\n".join(input))
    result = parser.validate_json(result)
    print(result) 

if __name__ == "__main__":
    main()