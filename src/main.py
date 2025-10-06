# import os
# import google.generativeai as genai
# from dotenv import load_dotenv
# from google.ai.generativelanguage_v1.types import content
# from pptx import Presentation
# from pptx.util import Inches, Pt
# from pptx.enum.text import PP_ALIGN
# from pptx.dml.color import RGBColor
# import requests
# from PIL import Image
# import io
# import json
#
# print(load_dotenv())
#
#
# class PPTGenerator:
#     def __init__(self, api_key=None):
#         self.api_key = api_key
#         if not self.api_key:
#             raise ValueError("Gemini API Key not there.")
#
#         genai.configure(api_key=self.api_key)
#         self.model = genai.GenerativeModel('gemini-2.5-pro')
#         self.model_vision = genai.GenerativeModel('gemini-2.5-pro')
#
#         self.presentation = Presentation()
#
#     def generate_content_outline(self, topic, num_slides=5):
#         """
#         Generate content outline using Genai
#         :param topic:
#         :param num_slides:
#         :return: json structure
#         """
#         prompt = f"""
#         Create a detailed outline for a PowerPoint presentation on "{topic}" with {num_slides}" slides.
#             Return the response as a JSON array with the following structure:
#             [
#                 {{
#                     "title"      : "Slide Title",
#                     "content"    : "Main content points as bullet points",
#                     "slide_type" : "title|content|image|conclusion"
#                 }}
#             ]
#
#             Make sure the content is engaging, informative, and well-structured.
#             The response must be a valid JSON array.
#             """
#
#         try:
#             response = self.model.generate_content(prompt)
#             content = response.text.strip()
#
#             if "```json" in content:
#                 content = content.split("```json")[1].split("```")[0].strip()
#             elif "```" in content:
#                 content = content.split("```")[1].strip()
#
#             if not content.startswith('[') or not content.endswith(']'):
#                 return None
#
#             try:
#                 return json.loads(content)
#             except json.JSONDecodeError as e:
#                 print(e)
#
#         except Exception as e:
#             print(e)
#             return None
#
#     def generate_image_description(self, slide_content):
#         prompt = f"""
#         Based on the slide content, suggest a relevant image description that would enhance the presentation.
#         {slide_content}
#         Return only a brief, descriptive phrase suitable for image search (max 5 words)
#         """
#         try:
#             response = self.model.generate_content(prompt)
#             content = response.text.strip()
#             return content
#         except Exception as e:
#             print(e)
#             return "professional presentation"
#
#     def download_imgae(self, query, save_path="temp_image.jpg"):
#         try:
#             url = "https://api.pexels.com/v1/search"
#             headers = {
#                 "Authorization": ""
#             }
#
#             params = {
#                 "query": query,
#                 "per_page": 1,
#                 "orientation": "landscape"
#             }
#
#             response = requests.get(url, headers=headers, params=params)
#             response.raise_for_status()
#
#             data = response.json()
#             if not data.get('photo'):
#                 raise ValueError("No photos found")
#
#             image_url = data['photos'][0]['src']['original']
#             image_response = requests.get(image_url)
#
#             with open(save_path, 'wb') as f:
#                 f.write(image_response.content)
#
#             return save_path
#
#         except Exception as e:
#             print(e)
#             return None
#
#     def create_title_slide(self, title, subtitle=""):
#         slide_layout = self.presentation.slide_layouts[0]
#         slide = self.presentation.slides.add_slide(slide_layout)
#
#         title_shape = slide.shape.title
#         title_shape.text = title
#         title_shape.text_frame.paragraphs[0].font.size = Pt(30)
#         title_shape.text_frame.paragraphs[0].font.bold = True
#         title_shape.text_frame.paragraphs[0].font.color.rgb = RGBColor(0,0,0)
#         title_shape.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
#
#         if subtitle:
#             subtitle_shape = slide.placeholders[1]
#             subtitle_shape.text = subtitle
#             subtitle_shape.text_frame.paragraphs[0].font.size = Pt(20)
#             subtitle_shape.text_frame.paragraphs[0].font.color.rgb = RGBColor(0, 0, 0)
#             subtitle_shape.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
#
#     def create_content_slide(self, title, content, include_image=None):
#         slide_layout = self.presentation.slide_layouts[1]
#         slide = self.presentation.slides.add_slide(slide_layout)
#
#         title_shape = slide.shape.title
#         title_shape.text = title
#         title_shape.text_frame.paragraphs[0].font.size = Pt(30)
#         title_shape.text_frame.paragraphs[0].font.bold = True
#
#         content_shape = slide.placeholders[1]
#         content_shape.text = content
#
#         text_frame = content_shape.text_frame
#         for paragraph in text_frame.paragraphs:
#             paragraph.font.size = Pt(20)
#             paragraph.font.color = RGBColor(0,0,0)
#
#         if include_image:
#             try:
#                 image_desc = self.generate_image_description(content)
#                 image_path = self.download_imgae(image_desc)
#                 if image_path and os.path.exists(image_path):
#                     slide.shapes.add_picture(image_path, Inches(6), Inches(2), height=(4))
#                     os.remove(image_path)
#             except Exception as e:
#                 print(e)
#
#             return slide
#
#     def create_image_slide(self, title, image_query):
#         slide_layout = self.presentation.slide_layouts[1]
#         slide = self.presentation.slides.add_slide(slide_layout)
#
#         title_box = slide.shapes.add_textbox(Inches(1), Inches(8), Inches(1))
#         title_frame = title_box.text_frame
#         title_frame.text = title
#         title_frame.text_frame.paragraphs[0].font.size = Pt(30)
#         title_frame.text_frame.paragraphs[0].font.bold = True
#         title_frame.text_frame.paragraphs[0].font.color.rgb = RGBColor(0,0,0)
#         title_frame.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
#
#         content_box = slide.shapes.add_textbox(Inches(0.5), Inches(2), Inches(4), Inches(5))
#         content_frame = content_box.text_frame
#         content_frame.text = content
#
#         for paragraph in content_frame.paragraphs:
#             paragraph.font.size = Pt(20)
#             paragraph.font.color.rgb = RGBColor(51, 51, 51)
#
#         try:
#             image_path = self.download_imgae(image_query)
#             if image_path and os.path.exists(image_path):
#                 slide.shapes.add_picture(image_path, Inches(6), Inches(2), height=Inches(4))
#                 os.remove(image_path)
#         except Exception as e:
#             print(e)
#
#         return slide
#
#     def generate_presentation(self, topic, num_slide=5, output_file="presentation.pptx"):
#         content_outline = self.generate_content_outline(topic, num_slide)
#
#         for i, slide_data in enumerate(content_outline):
#             title = slide_data["title"]
#             content = slide_data["content"]
#             slide_type = slide_data["slide_type"]
#
#             print(f"Creating slide {i+1}")
#
#             if slide_type == "title":
#                 self.create_title_slide(title, "Created by zeel")
#
#             elif slide_type == "image":
#                 img_query = self.generate_image_description(content)
#                 self.create_image_slide(title, img_query)
#
#             else:
#                 include_image = (i%3 == 0)
#                 self.create_content_slide(title, include_image)
#
#         self.presentation.save(output_file)
#         print(f"Presentation saved to {output_file}")
#
#         return output_file
#
#
# print("Generation done")
#
# api_key = ""
# try:
#     generator = PPTGenerator(api_key=api_key)
# except Exception as e:
#     print(e)
#
#     topic = "Artificial Intelligence in Healthcare"
#     num_slides = 6
#
# try:
#     output_file = generator.generate_presentation(topic,num_slides, "ai_healthcare.pptx")
# except Exception as e:
#     print(e)


import os
from dotenv import load_dotenv
from services.ppt_service import PPTGenerator

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("Gemini API Key not found in .env file.")

    generator = PPTGenerator(api_key=api_key)

    topic = "types of llm models"
    num_slides = 6

    try:
        output_file = generator.generate_presentation(topic, num_slides, "types_of_llm.pptx")
        print(f"✅ Presentation generated at: {output_file}")
    except Exception as e:
        print(f"❌ Error generating presentation: {e}")
