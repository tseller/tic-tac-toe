import vertexai
from vertexai.generative_models import GenerativeModel
from vertexai.preview.vision_models import ImageGenerationModel
from floggit import flog

PROJECT_ID = "learned-grammar-426001-g1"
vertexai.init(project=PROJECT_ID, location="us-west1")

image_model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-001")
@flog
def generate_image(prompt):
    response = image_model.generate_images(prompt)
    return response.images[0].show()

model = GenerativeModel("gemini-1.5-flash-002")
@flog
def generate_content(prompt):
    response = model.generate_content(prompt)
    return response.text