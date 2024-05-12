class PatientData:
    def __init__(self, Hour, HR, O2Sat, Temp, SBP, MAP, DBP, Resp, EtCO2, BaseExcess, HCO3, FiO2, pH, PaCO2, SaO2, AST,
                 BUN, Alkalinephos, Calcium, Chloride, Creatinine, Bilirubin_direct, Glucose, Lactate, Magnesium,
                 Phosphate, Potassium, Bilirubin_total, TroponinI, Hct, Hgb, PTT, WBC, Fibrinogen, Platelets, Age,
                 Gender, Unit1, Unit2, HospAdmTime, ICULOS, SepsisLabel, Patient_ID):
        self.Hour = Hour
        self.HR = HR
        self.O2Sat = O2Sat
        self.Temp = Temp
        self.SBP = SBP
        self.MAP = MAP
        self.DBP = DBP
        self.Resp = Resp
        self.EtCO2 = EtCO2
        self.BaseExcess = BaseExcess
        self.HCO3 = HCO3
        self.FiO2 = FiO2
        self.pH = pH
        self.PaCO2 = PaCO2
        self.SaO2 = SaO2
        self.AST = AST
        self.BUN = BUN
        self.Alkalinephos = Alkalinephos
        self.Calcium = Calcium
        self.Chloride = Chloride
        self.Creatinine = Creatinine
        self.Bilirubin_direct = Bilirubin_direct
        self.Glucose = Glucose
        self.Lactate = Lactate
        self.Magnesium = Magnesium
        self.Phosphate = Phosphate
        self.Potassium = Potassium
        self.Bilirubin_total = Bilirubin_total
        self.TroponinI = TroponinI
        self.Hct = Hct
        self.Hgb = Hgb
        self.PTT = PTT
        self.WBC = WBC
        self.Fibrinogen = Fibrinogen
        self.Platelets = Platelets
        self.Age = Age
        self.Gender = Gender
        self.Unit1 = Unit1
        self.Unit2 = Unit2
        self.HospAdmTime = HospAdmTime
        self.ICULOS = ICULOS
        self.SepsisLabel = SepsisLabel
        self.Patient_ID = Patient_ID

    def to_dict(self):
        return {
            "Hour": self.Hour,
            "HR": self.HR,
            "O2Sat": self.O2Sat,
            "Temp": self.Temp,
            "SBP": self.SBP,
            "MAP": self.MAP,
            "DBP": self.DBP,
            "Resp": self.Resp,
            "EtCO2": self.EtCO2,
            "BaseExcess": self.BaseExcess,
            "HCO3": self.HCO3,
            "FiO2": self.FiO2,
            "pH": self.pH,
            "PaCO2": self.PaCO2,
            "SaO2": self.SaO2,
            "AST": self.AST,
            "BUN": self.BUN,
            "Alkalinephos": self.Alkalinephos,
            "Calcium": self.Calcium,
            "Chloride": self.Chloride,
            "Creatinine": self.Creatinine,
            "Bilirubin_direct": self.Bilirubin_direct,
            "Glucose": self.Glucose,
            "Lactate": self.Lactate,
            "Magnesium": self.Magnesium,
            "Phosphate": self.Phosphate,
            "Potassium": self.Potassium,
            "Bilirubin_total": self.Bilirubin_total,
            "TroponinI": self.TroponinI,
            "Hct": self.Hct,
            "Hgb": self.Hgb,
            "PTT": self.PTT,
            "WBC": self.WBC,
            "Fibrinogen": self.Fibrinogen,
            "Platelets": self.Platelets,
            "Age": self.Age,
            "Gender": self.Gender,
            "Unit1": self.Unit1,
            "Unit2": self.Unit2,
            "HospAdmTime": self.HospAdmTime,
            "ICULOS": self.ICULOS,
            "SepsisLabel": self.SepsisLabel,
            "Patient_ID": self.Patient_ID
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            Hour=data["Hour"],
            HR=data["HR"],
            O2Sat=data["O2Sat"],
            Temp=data["Temp"],
            SBP=data["SBP"],
            MAP=data["MAP"],
            DBP=data["DBP"],
            Resp=data["Resp"],
            EtCO2=data["EtCO2"],
            BaseExcess=data["BaseExcess"],
            HCO3=data["HCO3"],
            FiO2=data["FiO2"],
            pH=data["pH"],
            PaCO2=data["PaCO2"],
            SaO2=data["SaO2"],
            AST=data["AST"],
            BUN=data["BUN"],
            Alkalinephos=data["Alkalinephos"],
            Calcium=data["Calcium"],
            Chloride=data["Chloride"],
            Creatinine=data["Creatinine"],
            Bilirubin_direct=data["Bilirubin_direct"],
            Glucose=data["Glucose"],
            Lactate=data["Lactate"],
            Magnesium=data["Magnesium"],
            Phosphate=data["Phosphate"],
            Potassium=data["Potassium"],
            Bilirubin_total=data["Bilirubin_total"],
            TroponinI=data["TroponinI"],
            Hct=data["Hct"],
            Hgb=data["Hgb"],
            PTT=data["PTT"],
            WBC=data["WBC"],
            Fibrinogen=data["Fibrinogen"],
            Platelets=data["Platelets"],
            Age=data["Age"],
            Gender=data["Gender"],
            Unit1=data["Unit1"],
            Unit2=data["Unit2"],
            HospAdmTime=data["HospAdmTime"],
            ICULOS=data["ICULOS"],
            SepsisLabel=data["SepsisLabel"],
            Patient_ID=data["Patient_ID"]
        )


