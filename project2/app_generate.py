
class Prompter:
    def __init__(self):
        self.system =None
        self.human = None
        self.ai = None 

    def __str__(self):
        return f"System ={self.system}\nHuman = {self.human}\nAI Prompt = {self.ai}"


class PromptBuilder:
    def __init__(self):
        self.prompt = Prompter()

    def system_prompt(self, text):
        self.prompt.system = text 
        return self 
    
    def human_prompt(self, text):
        self.prompt.human = text 
        return self 
    
    def ai_prompt(self, text):
        self.prompt.ai = text
        return self 
    
    def get_prompt(self):
        return self.prompt
    
    def clear(self):
        self.prompt.system = None
        self.prompt.human = None
        self.prompt.ai = None
    
 

 


