class PatientRepository:
    def __init__(self):
        self._patients = {
            10: {"name": "Alice", "blocked": False, "financial_pending": False},
            20: {"name": "Beto", "blocked": True, "financial_pending": False},
            30: {"name": "Clara", "blocked": False, "financial_pending": True},
            40: {"name": "Diego", "blocked": False, "financial_pending": False},
            50: {"name": "Eva", "blocked": False, "financial_pending": False},
        }

    def exists(self, patient_id: int) -> bool:
        return patient_id in self._patients

    def is_blocked(self, patient_id: int) -> bool:
        if patient_id not in self._patients:
            return False
        return self._patients[patient_id]["blocked"]

    def has_financial_pending(self, patient_id: int) -> bool:
        if patient_id not in self._patients:
            return False
        return self._patients[patient_id]["financial_pending"]
