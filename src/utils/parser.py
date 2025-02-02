from pydantic import BaseModel
from typing import Any, List, Union

# Define the schema for different types of data

class Object(BaseModel):
    """Schema for object data"""
    name: str
    
class PickUp(BaseModel):
    """Schema for pick_up data"""
    object: Object
    
class PutDown(BaseModel):
    """Schema for put_down data"""
    object: Object
    
class Commands(BaseModel):
    """Schema for commands data"""
    actions: list[Union[PickUp, PutDown]] # List of all types of actions

class Parser:
    def __init__(self):
        pass
    
    def validate_json(self, json_data):
        """Validate the json data
        
        Args:
            json_data (dict): The json data to be validated
        """
        
        return Commands.model_validate_json(json_data)