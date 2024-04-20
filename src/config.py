"""Common configuration variables for the application."""

DOCTORS = ["Csaba", "Gabor", "Szabolcs", "Sumair", "Mehdi", "Ali"]
GENDERS = ["Male", "Female"]
WARD_NUMBERS = [1, 2, 3, 4]
ROOM_NUMBERS = {ward: [f"{ward}{room}" for room in range(10)] for ward in WARD_NUMBERS}
API_CONTROLLER_URL = "http://127.0.0.1:5000"
