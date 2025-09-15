import json

class AIGenerator:
    def __init__(self, sample_file):
        with open(sample_file, 'r') as f:
            self.sample_data = json.load(f)

    def generate(self, concept):
        # Return sample slides for given concept
        if self.sample_data['concept'] == concept:
            return self.sample_data['slides']
        else:
            return []

# Example usage
ai_gen = AIGenerator('data/sample_script.json')
slides = ai_gen.generate("Photosynthesis")
print(slides)


"""

this file will load script.json
and make slides for animation , it returns the associated slides, otherwise it returns an empty list.""
