class G_PatientData:
    def __init__(self, Age, Blood_Glucose_Level, Diastolic_Blood_Pressure, Systolic_Blood_Pressure, Heart_Rate, Body_Temperature, SPO2, Sweating, Shivering, Diabetic_NonDiabetic):
        self.Age = Age
        self.Blood_Glucose_Level = Blood_Glucose_Level
        self.Diastolic_Blood_Pressure = Diastolic_Blood_Pressure
        self.Systolic_Blood_Pressure = Systolic_Blood_Pressure
        self.Heart_Rate = Heart_Rate
        self.Body_Temperature = Body_Temperature
        self.SPO2 = SPO2
        self.Sweating = Sweating
        self.Shivering = Shivering
        self.Diabetic_NonDiabetic = Diabetic_NonDiabetic

    def to_dict(self):
        return {
            "Age": self.Age,
            "Blood_Glucose_Level": self.Blood_Glucose_Level,
            "Diastolic_Blood_Pressure": self.Diastolic_Blood_Pressure,
            "Systolic_Blood_Pressure": self.Systolic_Blood_Pressure,
            "Heart_Rate": self.Heart_Rate,
            "Body_Temperature": self.Body_Temperature,
            "SPO2": self.SPO2,
            "Sweating": self.Sweating,
            "Shivering": self.Shivering,
            "Diabetic_NonDiabetic": self.Diabetic_NonDiabetic
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            Age=data["Age"],
            Blood_Glucose_Level=data["Blood_Glucose_Level"],
            Diastolic_Blood_Pressure=data["Diastolic_Blood_Pressure"],
            Systolic_Blood_Pressure=data["Systolic_Blood_Pressure"],
            Heart_Rate=data["Heart_Rate"],
            Body_Temperature=data["Body_Temperature"],
            SPO2=data["SPO2"],
            Sweating=data["Sweating"],
            Shivering=data["Shivering"],
            Diabetic_NonDiabetic=data["Diabetic_NonDiabetic"]
        )

# Example usage:
data_row = {
    "Age": 39,
    "Blood_Glucose_Level": 80,
    "Diastolic_Blood_Pressure": 73,
    "Systolic_Blood_Pressure": 119,
    "Heart_Rate": 102,
    "Body_Temperature": 98.30070675,
    "SPO2": 94,
    "Sweating": 1,
    "Shivering": 0,
    "Diabetic_NonDiabetic": "N"
}

patient_instance = PatientData.from_dict(data_row)
print(patient_instance.to_dict())
