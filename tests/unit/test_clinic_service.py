import pytest
from unittest.mock import Mock
from src.clinic_service import ClinicService


def build_service():
    doctor_repository = Mock()
    patient_repository = Mock()
    appointment_repository = Mock()
    waitlist_repository = Mock()

    return ClinicService(
        doctor_repository,
        patient_repository,
        appointment_repository,
        waitlist_repository,
    ), doctor_repository, patient_repository, appointment_repository, waitlist_repository


def test_schedule_appointment_raises_when_parameters_are_missing():
    service, *_ = build_service()

    with pytest.raises(ValueError, match="Patient ID, doctor ID and slot are required"):
        service.schedule_appointment(None, 1, "2026-06-10 09:00")


def test_schedule_appointment_returns_false_when_patient_does_not_exist():
    service, doctor_repository, patient_repository, appointment_repository, waitlist_repository = build_service()
    patient_repository.exists.return_value = False

    result = service.schedule_appointment(999, 1, "2026-06-10 09:00")

    assert result is False


def test_schedule_appointment_creates_appointment_when_possible():
    service, doctor_repository, patient_repository, appointment_repository, waitlist_repository = build_service()

    patient_repository.exists.return_value = True
    doctor_repository.exists.return_value = True
    patient_repository.is_blocked.return_value = False
    patient_repository.has_financial_pending.return_value = False
    appointment_repository.count_active_appointments.return_value = 0
    appointment_repository.has_appointment.return_value = False
    appointment_repository.is_slot_taken.return_value = False

    result = service.schedule_appointment(10, 1, "2026-06-10 09:00")

    assert result is True
    appointment_repository.create_appointment.assert_called_once_with(10, 1, "2026-06-10 09:00")
    waitlist_repository.remove_entry.assert_called_once_with(10, 1, "2026-06-10 09:00")


def test_join_waitlist_returns_false_when_slot_is_free():
    service, doctor_repository, patient_repository, appointment_repository, waitlist_repository = build_service()

    patient_repository.exists.return_value = True
    doctor_repository.exists.return_value = True
    patient_repository.is_blocked.return_value = False
    appointment_repository.is_slot_taken.return_value = False

    result = service.join_waitlist(10, 1, "2026-06-10 09:00")

    assert result is False


def test_cancel_appointment_promotes_first_waitlisted_patient():
    service, doctor_repository, patient_repository, appointment_repository, waitlist_repository = build_service()

    appointment_repository.has_appointment.return_value = True
    waitlist_repository.next_patient.return_value = 40

    result = service.cancel_appointment(10, 1, "2026-06-10 09:00")

    assert result is True
    appointment_repository.cancel_appointment.assert_called_once_with(10, 1, "2026-06-10 09:00")
    appointment_repository.create_appointment.assert_called_once_with(40, 1, "2026-06-10 09:00")
    waitlist_repository.remove_entry.assert_called_once_with(40, 1, "2026-06-10 09:00")
