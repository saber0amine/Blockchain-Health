import tkinter as tk
from tkinter import scrolledtext
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

# Expanded symptom to specialty mapping
symptom_specialty_map = {
    'fever': 'Internal Medicine',
    'cough': 'Pulmonology',
    'headache': 'Neurology',
    'abdominal pain': 'Gastroenterology',
    'chest pain': 'Cardiology',
    'rash': 'Dermatology',
    'kidney': 'Nephrology',
    'diabetes': 'Endocrinology',
    'sepsis': 'Critical Care Medicine',
    # Add more symptoms and specialties as needed
}

# Sample doctor database (name, specialty, contact info)
doctor_database = [
    {'name': 'Dr. John Smith', 'specialty': 'Internal Medicine', 'contact': '123-456-7890'},
    {'name': 'Dr. Emily Johnson', 'specialty': 'Pulmonology', 'contact': '234-567-8901'},
    {'name': 'Dr. Watson Dalock', 'specialty': 'Nephrology', 'contact': '345-678-9012'},
    {'name': 'Dr. Mo Ishoe', 'specialty': 'Endocrinology', 'contact': '456-789-0123'},
    {'name': 'Dr. Eve Isblack', 'specialty': 'Critical Care Medicine', 'contact': '567-890-1234'},
    {'name': 'Dr. Michael Lee', 'specialty': 'Neurology', 'contact': '678-901-2345'},
    {'name': 'Dr. Sarah Patel', 'specialty': 'Gastroenterology', 'contact': '789-012-3456'},
    {'name': 'Dr. David Brown', 'specialty': 'Cardiology', 'contact': '890-123-4567'},
    {'name': 'Dr. Jennifer White', 'specialty': 'Dermatology', 'contact': '901-234-5678'},
]


class MedicalChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DoctorX")

        self.chat_history = scrolledtext.ScrolledText(root, width=50, height=20)
        self.chat_history.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.input_label = tk.Label(root, text="Enter your symptoms:")
        self.input_label.grid(row=1, column=0, padx=10, pady=5)

        self.input_entry = tk.Entry(root, width=40)
        self.input_entry.grid(row=1, column=1, padx=10, pady=5)

        self.submit_button = tk.Button(root, text="Submit", command=self.submit)
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.model_label = tk.Label(root, text="Recommended Model:")
        self.model_label.grid(row=3, column=0, padx=10, pady=5)

        self.model_text = tk.Text(root, width=40, height=2)
        self.model_text.grid(row=3, column=1, padx=10, pady=5)

    def submit(self):
        symptoms = self.input_entry.get()
        specialty = self.recommend_specialty(symptoms)
        if specialty:
            response = f"Based on your symptoms, you should consider seeing a {specialty} specialist."
            doctor = self.recommend_doctor(specialty)
            model = self.recommend_model(specialty)
            if doctor:
                response += f" We recommend Dr. {doctor['name']}. Contact: {doctor['contact']}"
            else:
                response += " Unfortunately, we couldn't find a doctor specializing in this field."
            if model:
                response += f" We also suggest using the {model} model for diagnosis."
        else:
            response = "I'm sorry, I couldn't determine a suitable specialty based on your symptoms."
        self.display_response(response)

    def recommend_specialty(self, symptoms):
        tokens = word_tokenize(symptoms)
        filtered_tokens = [word for word in tokens if word.lower() not in stopwords.words('english')]
        symptoms = [word.lower() for word in filtered_tokens if word.lower() in symptom_specialty_map]
        for symptom in symptoms:
            if symptom in symptom_specialty_map:
                return symptom_specialty_map[symptom]
        return None

    def recommend_doctor(self, specialty):
        for doctor in doctor_database:
            if doctor['specialty'] == specialty:
                return doctor
        return None

    def recommend_model(self, specialty):
        our_models = {'Nephrology': 'glucose_model',
                      'Endocrinology': 'kidneydiseases_model',
                      'Critical Care Medicine': 'Sepsis_model'}
        if specialty in our_models:
            return our_models[specialty]
        else:
            return None

    def display_response(self, response):
        self.chat_history.insert(tk.END, response + "\n\n")
        self.chat_history.see(tk.END)


def main():
    root = tk.Tk()
    app = MedicalChatbotGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
