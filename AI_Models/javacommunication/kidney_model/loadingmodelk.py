import joblib

def load_model(model_path):
    # Load the trained model
    model = joblib.load(model_path)
    return model

def predict(model, features):
    # Make predictions using the loaded model
    predictions = model.predict(features)
    return predictions

if __name__ == "__main__":
    # Path to the trained model file
    model_path = "XGBClassifier.joblib"

    # Load the model
    model = load_model(model_path)

    # Example features for prediction (replace with your own features)
    features = [[9, 79, 73, 118, 98, 98.30070675, 99, 0, 0],
                [9, 80, 73, 119, 102, 98.30070675, 94, 1, 0],
                # Add more feature vectors as needed
               ]

    # Make predictions
    predictions = predict(model, features)
    print("Predictions:", predictions)
