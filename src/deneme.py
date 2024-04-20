import requests

# ************ hello world
def hello_world():
	uri = "http://127.0.0.1:5000/hello"

	response = requests.get(uri)
	print('HELLO WORLD response:::', response.json())

# ************ all patients
def all_patients():
	uri = "http://127.0.0.1:5000/patients"

	response = requests.get(uri)
	print('ALL PATIENTS response:::', response.json())


# ************ PATIENT WITH ID
def spesific_patient():
	uri = "http://127.0.0.1:5000/patients/30ed4a02-40e0-40a5-a939-e7f38a81acac"

	response = requests.get(uri)
	if response.status_code == 200:
		print("SPESIFIC PATIENT response id:::", response.json()["patient"]["patient_id"])
	print('SPESIFIC PATIENT response:::', response.json())

# ************ create patient
def create_patient():
	payload = {
		"patient_id": "30ed4a02-40e0-40a5-a939-e7f38a81acac",
		"patient_name": "test-patient",
		"patient_age": 23,
		"patient_gender": "Male",
		"patient_checkin": "2024-03-23 21:32:07.071378",
		"patient_checkout": "None",
		"patient_ward": 1,
		"patient_room": 15
	}

	uri = "http://127.0.0.1:5000/patients"

	response = requests.post(uri, json=payload)
	print('CREATE PATIENT response:::', response.json())

# ************ delete patient

def delete_patient():
	uri = "http://127.0.0.1:5000/patient/30ed4a02-40e0-40a5-a939-e7f38a81acac"

	response = requests.delete(uri)
	print('DELETE PATIENT response:::', response.json())

# **************************************************************
# **************************************************************
# **************************************************************
# **************************************************************
# **************************************************************
# **************************************************************


hello_world()
all_patients()
spesific_patient()
# create_patient()
delete_patient()
# create_patient()