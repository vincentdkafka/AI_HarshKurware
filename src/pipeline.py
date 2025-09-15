from knowledge_graph import KnowledgeGraph
from ai_generator import AIGenerator
from formatter import Formatter
from manim_animation import create_animation

def main(concept):
    kg = KnowledgeGraph('data/knowledge_graph_sample.json')
    ai_gen = AIGenerator('data/sample_script.json')
    formatter = Formatter()

    slides = ai_gen.generate(concept)
    formatted_slides = formatter.format(slides)

    create_animation(formatted_slides)
    print(f"Video for {concept} generated in output/")

if __name__ == "__main__":
    main("Photosynthesis")


"""

this file is main piepline where everything is orchestrated
"""
