# app.py

from py4j.java_gateway import JavaGateway
from loadingmodelg import Model_forglucose

# Load the model
model = Model_forglucose("XGBClassifier2lastone.joblib")

# Start the Py4J gateway server
gateway = JavaGateway()
gateway.entry_point.registerModel(model)
