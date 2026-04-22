import pytest
from src.appointment_repository import AppointmentRepository


def test_create_appointment_registers_new_appointment():
    repository = AppointmentRepository()
    repository.create_appointment(10, 1, "2026-06-10 09:00")
    assert repository.has_appointment(10, 1, "2026-06-10 09:00") is True


def test_create_appointment_raises_for_duplicate():
    repository = AppointmentRepository()
    repository.create_appointment(10, 1, "2026-06-10 09:00")

    with pytest.raises(ValueError, match="Appointment already exists"):
        repository.create_appointment(10, 1, "2026-06-10 09:00")


def test_is_slot_taken_returns_true_when_doctor_has_appointment_in_slot():
    repository = AppointmentRepository()
    repository.create_appointment(10, 1, "2026-06-10 09:00")
    assert repository.is_slot_taken(1, "2026-06-10 09:00") is True


def test_count_active_appointments_counts_patient_appointments():
    repository = AppointmentRepository()
    repository.create_appointment(10, 1, "2026-06-10 09:00")
    repository.create_appointment(10, 2, "2026-06-10 10:00")
    assert repository.count_active_appointments(10) == 2


def test_cancel_appointment_removes_existing_appointment():
    repository = AppointmentRepository()
    repository.create_appointment(10, 1, "2026-06-10 09:00")
    repository.cancel_appointment(10, 1, "2026-06-10 09:00")
    assert repository.has_appointment(10, 1, "2026-06-10 09:00") is False


def test_cancel_appointment_raises_for_missing_appointment():
    repository = AppointmentRepository()

    with pytest.raises(ValueError, match="Active appointment not found"):
        repository.cancel_appointment(10, 1, "2026-06-10 09:00")
