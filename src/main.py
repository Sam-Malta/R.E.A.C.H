# Description: Main file to run the code
from llm_integration.llm_handler import LLM_Handler

def main():
    print("Initializing main function")
    # Example usage
    handler = LLM_Handler()
    result = handler.predict("Say something funny")
    print(result) 

if __name__ == "__main__":
    main()