"""Patient API Controller"""

from flask import Flask, request, jsonify
from patient_db import PatientDB


class PatientAPIController:
	def __init__(self):
		self.app = Flask(__name__)
		self.patient_db = PatientDB()
		self.setup_routes()
		self.run()

	def setup_routes(self):
		"""
		Sets up the routes for the API endpoints.
		"""
		self.app.route("/hello", methods=["GET"])(self.hello_world)
		self.app.route("/patients", methods=["GET"])(self.get_patients)
		self.app.route("/patients/<patient_id>", methods=["GET"])(self.get_patient)
		self.app.route("/patients", methods=["POST"])(self.create_patient)
		self.app.route("/patient/<patient_id>", methods=["PUT"])(self.update_patient)
		self.app.route("/patient/<patient_id>", methods=["DELETE"])(self.delete_patient)


	"""
	TODO:
	Implement the following methods,
	use the self.patient_db object to interact with the database.

	Every method in this class should return a JSON response with status code
	Status code should be 200 if the operation was successful,
	Status code should be 400 if there was a client error,
	"""
    
	def hello_world(self):
		return jsonify({"message": "Hello, World!"}), 200

	def get_patients(self):
		return self.patient_db.select_all_patients()
		# print("patients:::", patients)
		# if patients is not None:
		# 	return jsonify({"patients", patients}), 200
		# else:
		# 	return jsonify({"error": "Patients couldn't be fetched from db."}), 400

	def get_patient(self, patient_id):
		patient =  self.patient_db.select_patient(patient_id=patient_id)
		if patient:
			return jsonify({"patient": patient}), 200
		else:
			return jsonify({"error": "No patient was found with the id of " + patient_id}), 400

	def create_patient(self):
		# print("******** request.json: ", request.json)
		# self.patient_db.insert_patient(request.json)
		"""
		Creates a new patient based on the data provided in the request body.
		"""
		data = request.json  # Access request body as JSON

		# Check if request body is empty
		if not data:
			return jsonify({"error": "No data provided in the request body"}), 400

		# Insert the patient into the database
		patient_id = self.patient_db.insert_patient(data)

		# Check if insertion was successful
		if patient_id:
			return jsonify({"message": "Patient created successfully", "patient_id": str(patient_id)}), 200
		else:
			return jsonify({"error": "Failed to create a new patient"}), 400

	def update_patient(self, patient_id):
		print("updatehaha:", patient_id, request.json)
		result = self.patient_db.update_patient(patient_id, request.json)
		
		if result:
			return jsonify({"message": "Patient with the given id is updated"}), 200
		else:
			return jsonify({"error":"Couldn't update the patient with the given id"}), 400

	def delete_patient(self, patient_id):
		result = self.patient_db.delete_patient(patient_id=patient_id)
		if result:
			return jsonify({"message": "The patient with the id of " + patient_id + " was deleted"}), 200
		else:
			return jsonify({"error": "Failed to delete a patient with the given id"}), 400

	def run(self):
		"""
		Runs the Flask application.
		"""
		self.app.run()


PatientAPIController()
