import pickle
import pandas as pd

# import the ML model
with open('model/model.pkl', 'rb') as file:
    model = pickle.load(file)

# MLFlow model version
# Note: In a real-world scenario, you would fetch this from MLFlow or your model
MODEL_VERSION = '1.0.0'

# Get the class labels from the model (important for matching probalities to class labels)
class_labels = model.classes_.tolist()

def predict_output(user_input : dict):

    input_df = pd.DataFrame([user_input])

    #predict the class
    predicted_class = model.predict(input_df)[0]

    #get the probabilities for all classes
    probabilities = model.predict_proba(input_df)[0]

    confidence = max(probabilities)

    # Create mapping: {class_label: probability}
    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities )))

    return {
        'predicted_category': predicted_class,
        'confidence': round(confidence, 4),
        'class_probabilities': class_probs
    }