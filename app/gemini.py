import vertexai
from vertexai.generative_models import GenerativeModel
from vertexai.preview.vision_models import ImageGenerationModel
from floggit import flog
from utils import random_string


PROJECT_ID = "learned-grammar-426001-g1"
vertexai.init(project=PROJECT_ID, location="us-west1")

generation_model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-001")
@flog
def generate_image(prompt):
    response = generation_model.generate_images(
            prompt=prompt, number_of_images=1)

    if response.images:
        filename = random_string() + ".jpg"
        response.images[0].save(filename)
        return filename

    return None


model = GenerativeModel("gemini-1.5-flash-002")
@flog
def generate_content(prompt):
    response = model.generate_content(prompt)
    return response.text
