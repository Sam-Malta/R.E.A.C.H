import ollama
from utils.parser import Commands

class LLM_Handler:
    def __init__(self, model_name='deepseek-r1'):
        self.model_name = model_name
        # Check if the model exists, if not pull it
        if not self.does_model_exist():
            print(f"Pulling model {self.model_name}...")
            ollama.pull(self.model_name)
            print(f"Model {self.model_name} pulled successfully")
        
        # Initialize the messages list
        self.messages = []
 
    def does_model_exist(self):
        """Check if the model exists
        
        Returns:
            bool: True if the model exists, False otherwise
        """
        
        models = ollama.list()
        for model in models.models:
            if model.model.split(':')[0] == self.model_name:
                return True
        return False
        
    def predict(self, input_data):
        """Send input data to the model and return the result
        
        Args:
            input_data (string): The input data to be passed to the model
        """
        
        try:
            self.messages.append({'role': 'user', 'content': input_data}) # Append the input data to the messages list
            
            # Send the input data to the model
            response = ollama.chat(
                model=self.model_name,
                messages=[{'role': 'user', 'content': input_data}],
                format=Commands.model_json_schema(),
                options={"temperature": 0}
            ) 
            
            self.messages.append({'role': 'assistant', 'content': response['message']['content']}) # Append the response to the messages list
            return response['message']['content']
        except Exception as e:
            print(f"Failed to get prediction from model {self.model_name}: {e}")
            return None
        
        
        

