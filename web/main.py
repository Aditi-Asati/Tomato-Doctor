import streamlit as st
import requests
import base64
from PIL import Image
from io import BytesIO


def get_base64(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = (
        """
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    """
        % bin_str
    )
    st.markdown(page_bg_img, unsafe_allow_html=True)


def create_image_border(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    # bin_str = get_base64(uploaded_file)
    image_html = f"""
    <div style="display: flex; justify-content: center; align-items: center;">
        <img src="data:image/png;base64,{img_str}" style="border: 5px solid black;">
    </div>
    """
    st.markdown(image_html, unsafe_allow_html=True)


set_background("./tomato_field.png")

# Render the HTML and CSS using Streamlit

FASTAPI_ENDPOINT = "http://localhost:8000/predict"

custom_css = """
<style>
/* Change the color of the title text */
h1 {
    color: #3d070b; /* Replace with your desired color */
}

/* Center the button */
div.stButton > button {
    display: block;
    margin: 0 auto;
}
</style>
"""

# Render the custom CSS using Streamlit
st.markdown(custom_css, unsafe_allow_html=True)


st.title("Tomato Leaf Disease Predictor")
# st.write("Upload an image of a tomato leaf here")
st.markdown('<p style="color: black; font-size: 20px">Upload an image of a tomato leaf here to predict its disease.</p>', unsafe_allow_html=True) 


uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    create_image_border(Image.open(BytesIO(uploaded_file.getvalue())))
    # st.image(image, caption="Uploaded Image", width=300)

    # Convert the image to bytes
    # img_byte_arr = BytesIO()
    # image.save(img_byte_arr, format=image.format)
    img_byte_arr = uploaded_file.getvalue()

    # Send the image to the FastAPI backend
    if st.button("Predict"):
        with st.spinner("Classifying..."):
            response = requests.post(
                FASTAPI_ENDPOINT,
                files={"file": ("filename", img_byte_arr, "image/jpeg")},
            )
            response.raise_for_status()
            if response.status_code == 200:
                result = response.json()
                html_content = f"""
                <div style="text-align: center; color: black; background-color: rgba(144, 238, 144, 0.3); padding: 10px; border-radius: 5px;">
                <strong>PREDICTED DISEASE :</strong> <span style="color: #170406;"><strong>{result['Label']}</strong></span><br><br>
                <strong>CONFIDENCE :</strong> <span style="color: #170406;"><strong>{result['Confidence']}%</strong></span>
                </div>
                """

                # Display the formatted content within st.success
                st.markdown(html_content, unsafe_allow_html=True)
                
            else:
                st.error("Error occurred while predicting.")
