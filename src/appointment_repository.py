class AppointmentRepository:
    def __init__(self):
        self._appointments = []

    def create_appointment(self, patient_id: int, doctor_id: int, slot: str) -> None:
        if self.has_appointment(patient_id, doctor_id, slot):
            raise ValueError("Appointment already exists")
        self._appointments.append(
            {"patient_id": patient_id, "doctor_id": doctor_id, "slot": slot}
        )

    def has_appointment(self, patient_id: int, doctor_id: int, slot: str) -> bool:
        return any(
            a["patient_id"] == patient_id
            and a["doctor_id"] == doctor_id
            and a["slot"] == slot
            for a in self._appointments
        )

    def is_slot_taken(self, doctor_id: int, slot: str) -> bool:
        return any(
            a["doctor_id"] == doctor_id and a["slot"] == slot
            for a in self._appointments
        )

    def count_active_appointments(self, patient_id: int) -> int:
        return sum(1 for a in self._appointments if a["patient_id"] == patient_id)

    def cancel_appointment(self, patient_id: int, doctor_id: int, slot: str) -> None:
        for index, appointment in enumerate(self._appointments):
            if (
                appointment["patient_id"] == patient_id
                and appointment["doctor_id"] == doctor_id
                and appointment["slot"] == slot
            ):
                del self._appointments[index]
                return
        raise ValueError("Active appointment not found")
