
# AI-Powered Knowledge Graph → Manim Animation Automation.🚀📚

## Project Overview
This project automates the creation of **educational animated videos** from knowledge-based content.
Students can input a **concept**, and the system generates slides, narration scripts, and converts them into a **fully animated video** using **Manim**.

The project combines **Knowledge Graphs, AI/ML-based content generation, and animation automation**, providing a scalable pipeline for educational content.

---

## Features (MVP)✨
- **Knowledge Graph Storage**: Organizes concepts and relationships for concept retrieval.  
- **AI Slide & Script Generation**: Generates slide titles, bullet points, and narration scripts.  
- **Slide & Script Formatter**: Structures AI output into a Manim-friendly format.  
- **Manim Animation Automation**: Generates animated educational videos from formatted slides.  
- **Pipeline Orchestration**: Ties all modules together from concept → video.  

---

## Folder Structure📁

```bash

AI-KG-Manim-Automation/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│ ├── knowledge_graph_sample.json # Sample knowledge graph
│ └── sample_script.json # Sample AI slide & script output
│
├── src/
│ ├── knowledge_graph.py # Load and query KG
│ ├── ai_generator.py # Generate slides & narration
│ ├── formatter.py # Format slides for Manim
│ ├── manim_animation.py # Create animated slides
│ └── pipeline.py # Orchestrator for full demo
│
├── output/
│ ├── architecture_diagram.png # High-level flowchart
| |── sample_output.png # Screenshot of output




```

---

## How the MVP Works ⚙️

### 1. User Input
- Student provides a **concept** (Currently it is hard coded. and given data can fed to manim).

### 2. Knowledge Graph Query
- Retrieves related concepts and subgraph from `knowledge_graph_sample.json`.

### 3. AI Slide & Script Generation
- Converts KG subgraph into **slides with titles, bullet points, and narration**.  
- For MVP, uses `sample_script.json` as mock AI output.

### 4. Slide & Script Formatting
- Formats AI output into **Manim-readable JSON/dict**.

### 5. Animation with Manim
- Reads formatted slides.  
- Generates animated slides with text, bullet points, and optional diagrams.  
- Outputs video to `output/sample_video.mp4`.

### 6. Output & Viewing
- Students can **watch the final animated explanation** of the concept.

---

## Requirements

- manim==0.17.2      -> Animation engine: converts slides/scripts into animated videos
- networkx==3.1      -> Graph library: builds & queries knowledge graph of concepts
- numpy==1.26.0      -> Numerical computing: handles arrays, embeddings, and AI data
- pandas==2.1.0      -> Data handling: manages AI outputs, formats for Manim animation
- openai==1.0.0      -> AI module: generates slides, scripts, and explanations from concepts

---

 ## How to Run MVP
 
Clone Repository
```
git clone https://github.com/yourusername/AI-KG-Manim-Automation.git
cd AI-KG-Manim-Automation
Install Dependencies

pip install -r requirements.txt
Run Pipeline

python src/pipeline.py
View Output

Generated video saved in output/sample_video.mp4.

Sample Output
Example concept: "Photosynthesis"

AI generates slides, narration, and animated video.

Screenshot/video can be found in docs/sample_output.png or output/sample_video.mp4
```

---


## Future Scope
- Real-time AI integration for dynamic slide/script generation.

- Voiceovers / TTS for narration.

- Multi-language support for global learners.

- Interactive or domain-specific expansions (GIS, Space Tech, CS, Data Structures).

-Notes
MVP uses sample data to demonstrate functionality.

-Full-scale deployment can leverage real knowledge graphs from Wikidata or DBpedia.

-Manim rendering time depends on slide complexity; use caching or short clips for demos.


## Important
- MVP uses sample data to demonstrate functionality.

- Full-scale deployment can leverage real knowledge graphs from Wikidata or DBpedia.

- Manim rendering time depends on slide complexity; use caching or short clips for demos.

