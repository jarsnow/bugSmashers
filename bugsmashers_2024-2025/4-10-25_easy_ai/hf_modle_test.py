# slightly modified, from: https://huggingface.co/google/vit-base-patch16-224

from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image

# open image
image = Image.open('./pibble.jpeg')


processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
# gets a pretrained pytorch model from wherever specified
model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')

inputs = processor(images=image, return_tensors="pt")
outputs = model(**inputs)
logits = outputs.logits
# model predicts one of the 1000 ImageNet classes
predicted_class_idx = logits.argmax(-1).item()
print("Predicted class:", model.config.id2label[predicted_class_idx])
