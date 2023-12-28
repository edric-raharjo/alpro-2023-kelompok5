from roboflow import Roboflow

def predict_waldo(image_path):
    rf = Roboflow(api_key="8fyyMG4uiv0kffhT35Pk")
    project = rf.workspace().project("waldo-qa5u7")
    model = project.version("3").model

    # Infer on the uploaded image
    prediction = model.predict(image_path, confidence=40, overlap=30)
    predicted_image_path = "static/prediction.jpg"  # Save the predicted image in static folder

    prediction.save(predicted_image_path)
