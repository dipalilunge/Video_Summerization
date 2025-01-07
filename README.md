# Video_Summerization
video Summarisation based on query 

# Video Summarization Web Application

## Overview
This project implements a **Video Summarization Web Application** that uses **Flask** for the web interface and **PyTorch** for deep learning. The app allows users to upload videos and receive a summary based on a pre-trained video summarization model.

## Features
- Upload a video to receive a summarized output.
- Web interface powered by Flask.
- Deep learning model for video summarization using PyTorch.

## Technologies Used
- **Backend**: Flask
- **Deep Learning**: PyTorch
- **Frontend**: HTML
- **Libraries**: NumPy, OpenCV

## Installation Instructions
1. Clone the repository to your local machine.
2. Install the required dependencies listed in the `requirements.txt`.
3. Download the pre-trained model (`video_summarization_model.pth`) and place it in the project directory.
4. Run the Flask application to start the web server.

## Usage
Once the application is running, navigate to `http://127.0.0.1:5000/` in your web browser. You will be able to upload a video, and the system will generate a summarized output based on the video.

## Model Details
The summarization model is a deep learning-based PyTorch model that processes video input and generates a summarized version by analyzing key features from the video content.

