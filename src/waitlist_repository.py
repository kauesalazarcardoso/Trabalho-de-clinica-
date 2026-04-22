class WaitlistRepository:
    def __init__(self):
        self._entries = []

    def add_entry(self, patient_id: int, doctor_id: int, slot: str) -> None:
        if self.has_entry(patient_id, doctor_id, slot):
            raise ValueError("Waitlist entry already exists")
        self._entries.append(
            {"patient_id": patient_id, "doctor_id": doctor_id, "slot": slot}
        )

    def has_entry(self, patient_id: int, doctor_id: int, slot: str) -> bool:
        return any(
            e["patient_id"] == patient_id
            and e["doctor_id"] == doctor_id
            and e["slot"] == slot
            for e in self._entries
        )

    def has_any_entry(self, doctor_id: int, slot: str) -> bool:
        return any(
            e["doctor_id"] == doctor_id and e["slot"] == slot
            for e in self._entries
        )

    def next_patient(self, doctor_id: int, slot: str):
        for entry in self._entries:
            if entry["doctor_id"] == doctor_id and entry["slot"] == slot:
                return entry["patient_id"]
        return None

    def remove_entry(self, patient_id: int, doctor_id: int, slot: str) -> None:
        for index, entry in enumerate(self._entries):
            if (
                entry["patient_id"] == patient_id
                and entry["doctor_id"] == doctor_id
                and entry["slot"] == slot
            ):
                del self._entries[index]
                return
