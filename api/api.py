from fastapi import FastAPI, UploadFile
import uvicorn
from tensorflow import keras
# from keras.src import engine
import tensorflow as tf
# from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
from io import BytesIO
from PIL import Image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from pathlib import Path

app = FastAPI()

model_path = Path(__file__).parent.parent / "saved_models" / "tomato_model_version2.h5"
model = keras.models.load_model(
    str(model_path)
)
print("Successfully loaded the model!")

CLASSES = [
    "Bacterial spot",
    "Early blight",
    "Late blight",
    "Leaf Mold",
    "Septoria leaf spot",
    "Spider mites Two spotted spider mite",
    "Target Spot",
    "Tomato Yellow Leaf Curl Virus",
    "Tomato mosaic virus",
    "Healthy",
]


def get_predictions(img):
    predictions = model.predict(np.expand_dims(img, 0))
    predicted_label = CLASSES[np.argmax(predictions[0])]
    confidence = np.round(np.max(predictions) * 100, 2)
    return predicted_label, confidence


@app.post("/predict")
async def predict(file: UploadFile):
    img = np.array(Image.open(BytesIO(await file.read())))
    predicted_label, confidence = get_predictions(img)
    return {"Label": predicted_label, "Confidence": confidence}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
