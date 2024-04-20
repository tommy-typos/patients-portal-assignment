"""
Please import and use the config and db config variables.

The attributes for this class should be the same as the columns in the PATIENTS_TABLE.

The Object Arguments should only be name , gender and age.
Rest of the attributes should be set within the class.

-> for id use uuid4 to generate a unique id for each patient.
-> for checkin and checkout use the current date and time.

There should be a method to update the patient's room and ward. validation should be used.(config is given)

Validation should be done for all of the variables in config and db_config.

There should be a method to commit that patient to the database using the api_controller.
"""

from uuid import uuid4
from datetime import datetime
import requests
from config import API_CONTROLLER_URL, GENDERS, ROOM_NUMBERS, WARD_NUMBERS

class Patient:
	def __init__(self, name: str, gender: str, age: int):
		self.patient_id = str(uuid4())
		self.patient_name = self._validate_name(name)
		self.patient_gender = self._validate_gender(gender)
		self.patient_age = self._validate_age(age)
		self.patient_checkin = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
		self.patient_checkout = None
		self.patient_ward = None
		self.patient_room = None

	def _validate_name(self, name):
		if not isinstance(name, str):
			raise ValueError("Name must be a string.")
		return name

	def _validate_gender(self, gender):
		if gender not in GENDERS:
			raise ValueError("Invalid gender.")
		return gender

	def _validate_age(self, age):
		if not isinstance(age, int):
			raise ValueError("Age must be an integer.")
		if age < 0:
			raise ValueError("Age cannot be negative.")
		return age

	def set_ward(self, ward: int):
		if ward not in WARD_NUMBERS:
			raise ValueError("Invalid ward number.")
		self.patient_ward = ward

	def set_room(self, room: int):
		ward = int(room / 10)
		if str(room) not in ROOM_NUMBERS[ward]:
			raise ValueError("Invalid room number for the given ward.")
		self.patient_room = room

	def get_id(self):
		return self.patient_id

	def get_name(self):
		return self.patient_name

	def get_gender(self):
		return self.patient_gender

	def get_age(self):
		return self.patient_age

	def get_checkin(self):
		return self.patient_checkin

	def get_checkout(self):
		return self.patient_checkout

	def get_ward(self):
		return self.patient_ward

	def get_room(self):
		return self.patient_room

	def commit(self):
		response = requests.get(API_CONTROLLER_URL + "/patients/" + self.patient_id)
		patient_exist = None

		if response.status_code == 200:
			patient_exist = response.json()["patient"]["patient_id"] == self.patient_id

		if patient_exist:
			payload = {
				"patient_name": self.patient_name,
				"patient_age": self.patient_age,
				"patient_gender": self.patient_gender,
				"patient_checkin": self.patient_checkin,
				"patient_checkout": self.patient_checkout,
				"patient_ward": self.patient_ward,
				"patient_room": self.patient_room
			}
			response = requests.put(API_CONTROLLER_URL + "/patient/" + self.patient_id, json=payload)
			if response.status_code == 200:
				print("Successfully updated the patient: ", self.patient_id)
			else:
				print("Failed to update the patient: ", self.patient_id)
		else:
			payload = {
				"patient_id": self.patient_id,
				"patient_name": self.patient_name,
				"patient_age": self.patient_age,
				"patient_gender": self.patient_gender,
				"patient_checkin": self.patient_checkin,
				"patient_checkout": self.patient_checkout,
				"patient_ward": self.patient_ward,
				"patient_room": self.patient_room
			}
			response = requests.post(API_CONTROLLER_URL + "/patients", json=payload)
			if response.status_code == 200:
				print("Successfully created a new patient: ", self.patient_id)
			else:
				print("Failed to create a new patient")