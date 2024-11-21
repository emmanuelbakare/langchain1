
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
    
def main():
    # build = PromptBuilder()
    # build.system_prompt("This is what is in the system").human_prompt("and what the human has").ai_prompt("This is AI Prompt")
    # print(build.get_prompt())
    build1 = PromptBuilder().system_prompt("This is what is in the system").human_prompt("and what the human has").ai_prompt("This is AI Prompt").get_prompt()
    build2 = PromptBuilder().system_prompt("2nd System").human_prompt("2nd what the human has").ai_prompt("2nd - This is AI Prompt").get_prompt()

    print(build1, build2)

if __name__ == "__main__":
    main()



