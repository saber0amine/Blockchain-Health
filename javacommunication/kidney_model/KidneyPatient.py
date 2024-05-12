class K_data:
    def __init__(self, CreatinineBaseline, eGFRBaseline, sBPBaseline, dBPBaseline, BMIBaseline, TimeToEventMonths, EventCKD35, TIME_YEAR):
        self.CreatinineBaseline = CreatinineBaseline
        self.eGFRBaseline = eGFRBaseline
        self.sBPBaseline = sBPBaseline
        self.dBPBaseline = dBPBaseline
        self.BMIBaseline = BMIBaseline
        self.TimeToEventMonths = TimeToEventMonths
        self.EventCKD35 = EventCKD35
        self.TIME_YEAR = TIME_YEAR

    def to_dict(self):
        return {
            "CreatinineBaseline": self.CreatinineBaseline,
            "eGFRBaseline": self.eGFRBaseline,
            "sBPBaseline": self.sBPBaseline,
            "dBPBaseline": self.dBPBaseline,
            "BMIBaseline": self.BMIBaseline,
            "TimeToEventMonths": self.TimeToEventMonths,
            "EventCKD35": self.EventCKD35,
            "TIME_YEAR": self.TIME_YEAR
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            CreatinineBaseline=data["CreatinineBaseline"],
            eGFRBaseline=data["eGFRBaseline"],
            sBPBaseline=data["sBPBaseline"],
            dBPBaseline=data["dBPBaseline"],
            BMIBaseline=data["BMIBaseline"],
            TimeToEventMonths=data["TimeToEventMonths"],
            EventCKD35=data["EventCKD35"],
            TIME_YEAR=data["TIME_YEAR"]
        )

# Example usage:
data_row = {
    "CreatinineBaseline": 0.8,
    "eGFRBaseline": 90,
    "sBPBaseline": 120,
    "dBPBaseline": 80,
    "BMIBaseline": 25,
    "TimeToEventMonths": 12,
    "EventCKD35": 0,
    "TIME_YEAR": 2019
}

dataset_instance = Dataset.from_dict(data_row)
print(dataset_instance.to_dict())
