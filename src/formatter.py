class Formatter:
    def format(self, slides):
        formatted_slides = []
        for slide in slides:
            formatted_slides.append({
                "title": slide['title'],
                "bullets": slide['bullets'],
                "narration": slide['narration']
            })
        return formatted_slides

# Example usage
formatter = Formatter()
formatted = formatter.format(slides)
print(formatted)

"""
this file is where data is fed to our manim library 
it format all the data and fed to to make animation"""
