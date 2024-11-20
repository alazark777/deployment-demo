import requests
import gradio as gr

# Define the function to send a POST request to the Flask server
def predict_churn(feature1, feature2, feature3):
    url = "http://127.0.0.1:5001/predict"  # Flask API endpoint
    data = {
        "feature1": feature1,
        "feature2": feature2,
        "feature3": feature3
    }
    
    try:
        response = requests.post(url, json=data)  # Send the POST request
        if response.status_code == 200:
            result = response.json()
            return f"Prediction: {result['prediction']}"
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error connecting to server: {str(e)}"

# Define the Gradio interface
inputs = [
    gr.Number(label="Feature 1"),
    gr.Number(label="Feature 2"),
    gr.Number(label="Feature 3"),
]
output = gr.Textbox(label="Buy Tendency Prediction")

# Create Gradio interface
interface = gr.Interface(
    fn=predict_churn, 
    inputs=inputs, 
    outputs=output, 
    title="Customer Buy tendency Prediction"
)
interface.launch()
