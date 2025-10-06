# import google.generativeai as genai
# import json
#
# class LLMService:
#     def __init__(self, api_key: str):
#         if not api_key:
#             raise ValueError("Gemini API Key not provided.")
#         genai.configure(api_key=api_key)
#         self.model = genai.GenerativeModel("gemini-2.5-pro")
#
#     def generate_content_outline(self, topic: str, num_slides: int = 5):
#         prompt = f"""
#         Create a detailed outline for a PowerPoint presentation on "{topic}" with {num_slides} slides.
#         Return the response as a JSON array with this structure:
#         [
#             {{
#                 "title"      : "Slide Title",
#                 "content"    : "Main content points as bullet points",
#                 "slide_type" : "title|content|image|conclusion"
#             }}
#         ]
#         """
#
#         response = self.model.generate_content(prompt)
#         content = response.text.strip()
#
#         if "```json" in content:
#             content = content.split("```json")[1].split("```")[0].strip()
#         elif "```" in content:
#             content = content.split("```")[1].strip()
#
#         return json.loads(content)
#
#     def generate_image_description(self, slide_content: str):
#         prompt = f"""
#         Based on this slide content, suggest a relevant image description (max 5 words).
#         {slide_content}
#         """
#         response = self.model.generate_content(prompt)
#         return response.text.strip()


import google.generativeai as genai
import json

class LLMService:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("Gemini API Key not provided.")
        genai.configure(api_key=api_key)
        # Use flash for higher quota; you can switch back to pro if needed
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_content_outline(self, topic: str, num_slides: int = 5):
        prompt = f"""
        Create a detailed outline for a PowerPoint presentation on "{topic}" with {num_slides} slides.
        Return the response as a JSON array with the following structure:
        [
          {{
            "title": "Slide Title",
            "content": "Main content points as bullet points",
            "slide_type": "title|content|image|conclusion",
            "image_query": "short description for image (max 5 words)"
          }}
        ]
        The response must be valid JSON.
        """
        try:
            response = self.model.generate_content(prompt)
            content = response.text.strip()

            if "```json" in content:
                content = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                content = content.split("```")[1].strip()

            return json.loads(content)
        except Exception as e:
            print(f"Error generating outline: {e}")
            return None

    def generate_image_description(self, slide_content: str):
        prompt = f"""
        Based on this slide content, suggest a relevant image description (max 5 words).
        {slide_content}
        """
        response = self.model.generate_content(prompt)
        return response.text.strip()