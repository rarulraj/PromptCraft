import openai
import random

class PromptCraft:
    def __init__(self, gpt3_api_key):
        self.story_elements = {
            'setting': ['a dark forest', 'an ancient castle', 'a bustling city', 'a mysterious cave'],
            'characters': ['a wise wizard', 'a brave knight', 'a mischievous rogue', 'a mystical creature'],
            'plot': ['uncover a hidden treasure', 'defeat an evil sorcerer', 'solve a magical mystery'],
        }
        self.gpt3_api_key = gpt3_api_key

    def generate_prompt(self):
        prompt = {
            'setting': random.choice(self.story_elements['setting']),
            'characters': random.choice(self.story_elements['characters']),
            'plot': random.choice(self.story_elements['plot']),
        }
        return prompt

    def generate_story(self, prompt):
        openai.api_key = self.gpt3_api_key
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Your quest begins in {prompt['setting']}. You encounter {prompt['characters']} on a mission to {prompt['plot']}.",
            max_tokens=200,
        )
        return response.choices[0].text.strip()


gpt3_api_key = "your_gpt3_api_key_here"
prompt_craft = PromptCraft(gpt3_api_key)


generated_prompt = prompt_craft.generate_prompt()


generated_story = prompt_craft.generate_story(generated_prompt)


print(generated_story)
