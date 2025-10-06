import pytest
from src.services.llm_service import LLMService
from src.agents.content_agent import ContentAgent

class DummyLLM:
    def generate_content_outline(self, topic, num_slides=3):
        return [
            {"title": "Intro", "content": "Overview of topic", "slide_type": "title", "image_query": "intro graphic"},
            {"title": "Details", "content": "Some details here", "slide_type": "content", "image_query": "data chart"},
            {"title": "Conclusion", "content": "Final thoughts", "slide_type": "conclusion", "image_query": "summary icon"}
        ]

class DummyImageService:
    def download_image(self, query):
        return None  # skip real image downloading in tests

def test_generate_presentation(tmp_path):
    llm = DummyLLM()
    agent = ContentAgent(llm_service=llm, image_service=DummyImageService())
    output_file = tmp_path / "test.pptx"
    result = agent.generate_presentation("Test Topic", 3, str(output_file))
    assert result == str(output_file)
    assert output_file.exists()
