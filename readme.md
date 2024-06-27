# Tomato Doctor

**Tomato Doctor: From leaves to insights**


## Table of Contents

- [Introduction](#introduction)
- [Project Demo](#project-demo)
- [Features](#features)
- [Installation](#installation)
- [API Usage](#api-usage)
- [Guidelines](#guidelines)
- [License](#license)


## Introduction

Tomato Doctor is an AI-driven application designed to assist gardeners, farmers, and agricultural professionals in diagnosing diseases in tomato plants. By simply uploading an image of a tomato leaf, Tomato Doctor can accurately predict the disease affecting the plant, providing a confidence value to help users understand the reliability of the diagnosis.

### Project Demo

Here is a demonstration of Tomato Doctor in action:

[![Tomato Doctor Demo](https://img.youtube.com/vi/mgK7v0i_HpI/0.jpg)](https://www.youtube.com/watch?v=mgK7v0i_HpI)


<!-- [![Tomato Doctor Demo](https://img.youtube.com/vi/dQw4w9WgXcQ/0.jpg)](https://www.youtube.com/watch?v=dQw4w9WgXcQ) -->

## Features

- **Disease Prediction**: Upload an image of a tomato leaf and receive an instant diagnosis of the disease.
- **Confidence Score**: Each prediction comes with a confidence score to indicate the accuracy of the diagnosis.
- **Comprehensive Disease Database**: Covers a wide range of common tomato plant diseases.
- **User-Friendly Interface**: Simple and intuitive interface for easy navigation and use.


## Installation

To get started with Tomato Doctor, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Aditi-Asati/Tomato-Doctor.git
    cd Tomato-Doctor
    ```

2. **Build Docker Image**:
    ```bash
    docker build -t Tomato-Doctor . 
    ```

## API Usage

Tomato Doctor has just one API endpoint to facilitate the classification of leaf disease through a FastAPI backend. Below are the details of this endpoint:

### 1. Submit Form

**Endpoint**: `POST http://localhost:8000/predict`

**Description**: This endpoint is used to get the disease prediction. It returns the predicted disease along with confidence.

**Request Body**:

It should contain the bytes array of uploaded image file. The `files` parameter in the `post` method is used to send this information.
```json
{"file": ("filename", img_byte_arr, "image/jpeg")}
```

**Response**:

The response will be a JSON object containing the predicted disease and the confidence value.
```json
{
    "disease": "Tomato Mosaic Virus",
    "confidence": 0.92
}

```

## Guidelines
1. **Start the Application**:
    ```bash
    docker run -p 8000:8000 -p 8501:8501 Tomato-Doctor
    ```

2. **Interact with Tomato Doctor**:
    - Use the interface to upload a tomato leaf image (format: jpg/ jpeg/ png).
    - Hit `Predict` button to get the disease prediction with confidence.


## License

Tomato Doctor is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for more details.

