from flask import Flask, render_template, request, redirect, url_for
from infer import predict_waldo  # Import the function
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/findwaldo')
def index():
    return render_template('dragndrop.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        os.remove("static/prediction.jpg")
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']

        if file.filename == '':
            return 'No selected file'

        img_link = "static/uploaded_image.jpg"  # Save the uploaded image in static folder
        file.save(img_link)

        # Run prediction function on the uploaded image
        predict_waldo(img_link)

        return redirect(url_for('show_prediction'))
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/prediction')
def show_prediction():
    return render_template('prediction.html')

if __name__ == '__main__':
    app.run(debug=True)
