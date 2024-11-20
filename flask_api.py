from flask import Flask, request, jsonify
import pickle

app=Flask(__name__)

pickle_in = open("logreg.pkl","rb")
model=pickle.load(pickle_in)


@app.route('/predict', methods=['POST'])
def predict():
    
    """Predict if Customer would buy the product or not .
    ---
    parameters:  
      - name: age
        in: query
        type: number
        required: true
      - name: new_user
        in: query
        type: number
        required: true
      - name: total_pages_visited
        in: query
        type: number
        required: true
      
    responses:
        500:
            description: Prediction
        
    """
    try:
      # Parse JSON data from the POST request
      data = request.get_json()

      # Extract features from the JSON payload
      age = int(data["feature1"])
      new_user = int(data["feature2"])
      total_pages_visited = int(data["feature3"])

      # Make prediction
      prediction = model.predict([[age, new_user, total_pages_visited]])

      # Return the result as JSON
      return jsonify({"prediction": int(prediction[0])}), 200
    except KeyError as e:
      return jsonify({"error": f"Missing key in request payload: {str(e)}"}), 400
    except Exception as e:
      return jsonify({"error": str(e)}), 500

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0', port=5001)