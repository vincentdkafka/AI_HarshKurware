from manim import *

class SlideScene(Scene):
    def construct(self, slide):
        title = Text(slide['title']).to_edge(UP)
        self.play(Write(title))
        for i, bullet in enumerate(slide['bullets']):
            b = Text(bullet).shift(DOWN*(i+1))
            self.play(Write(b))
        self.wait(2)

# Example usage: loop through slides
def create_animation(slides, output_file='output/sample_video.mp4'):
    for slide in slides:
        scene = SlideScene(slide)
        # In practice, you would use manim CLI or Python API to render



"""

main animation code will run here to create animation
Rendering Manim videos are usually created by CLI:
""
