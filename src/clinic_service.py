class ClinicService:
    def __init__(
        self,
        doctor_repository,
        patient_repository,
        appointment_repository,
        waitlist_repository,
    ):
        self.doctor_repository = doctor_repository
        self.patient_repository = patient_repository
        self.appointment_repository = appointment_repository
        self.waitlist_repository = waitlist_repository

    def schedule_appointment(self, patient_id: int, doctor_id: int, slot: str) -> bool:
        if not patient_id or not doctor_id or not slot:
            raise ValueError("Patient ID, doctor ID and slot are required")

        if not self.patient_repository.exists(patient_id):
            return False

        if not self.doctor_repository.exists(doctor_id):
            return False

        if self.patient_repository.is_blocked(patient_id):
            return False

        if self.patient_repository.has_financial_pending(patient_id):
            return False

        if self.appointment_repository.count_active_appointments(patient_id) >= 2:
            return False

        if self.appointment_repository.has_appointment(patient_id, doctor_id, slot):
            return False

        if self.appointment_repository.is_slot_taken(doctor_id, slot):
            return False

        self.appointment_repository.create_appointment(patient_id, doctor_id, slot)
        self.waitlist_repository.remove_entry(patient_id, doctor_id, slot)
        return True

    def join_waitlist(self, patient_id: int, doctor_id: int, slot: str) -> bool:
        if not patient_id or not doctor_id or not slot:
            raise ValueError("Patient ID, doctor ID and slot are required")

        if not self.patient_repository.exists(patient_id):
            return False

        if not self.doctor_repository.exists(doctor_id):
            return False

        if self.patient_repository.is_blocked(patient_id):
            return False

        if not self.appointment_repository.is_slot_taken(doctor_id, slot):
            return False

        if self.waitlist_repository.has_entry(patient_id, doctor_id, slot):
            return False

        if self.appointment_repository.has_appointment(patient_id, doctor_id, slot):
            return False

        self.waitlist_repository.add_entry(patient_id, doctor_id, slot)
        return True

    def cancel_appointment(self, patient_id: int, doctor_id: int, slot: str) -> bool:
        if not patient_id or not doctor_id or not slot:
            raise ValueError("Patient ID, doctor ID and slot are required")

        if not self.appointment_repository.has_appointment(patient_id, doctor_id, slot):
            return False

        self.appointment_repository.cancel_appointment(patient_id, doctor_id, slot)

        next_patient = self.waitlist_repository.next_patient(doctor_id, slot)
        if next_patient is not None:
            self.appointment_repository.create_appointment(next_patient, doctor_id, slot)
            self.waitlist_repository.remove_entry(next_patient, doctor_id, slot)

        return True
