from flask import Flask, request, render_template, jsonify
import torch
from model import load_model, CustomModel

app = Flask(__name__)

# Load the model
model = load_model('video_summarization_model.pth')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    # Get the data from the form
    video_data = request.files['video']
    
    # Assuming video_data is processed and turned into a tensor
    # For example, video_tensor = process_video(video_data)
    
    # Dummy data for demonstration (replace with actual video tensor)
    video_tensor = torch.randn(1, 1, 64, 64)  # Example tensor

    with torch.no_grad():
        summary = model(video_tensor)
    
    summary_text = summary.argmax(dim=1).item()  # Example output processing

    return jsonify({'summary': summary_text})

if __name__ == '__main__':
    app.run(debug=True)
