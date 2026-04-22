class DoctorRepository:
    def __init__(self):
        self._doctors = {
            1: {"name": "Dra. Ana"},
            2: {"name": "Dr. Bruno"},
            3: {"name": "Dra. Carla"},
        }

    def exists(self, doctor_id: int) -> bool:
        return doctor_id in self._doctors
