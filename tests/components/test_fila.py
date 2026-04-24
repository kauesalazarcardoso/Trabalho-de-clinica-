import pytest
from src.clinic_service import ClinicService
from src.appointment_repository import AppointmentRepository
from src.doctor_repository import DoctorRepository
from src.patient_repository import PatientRepository
from src.waitlist_repository import WaitlistRepository

def create_service():
    doctor_repo = DoctorRepository()
    patient_repo = PatientRepository()
    appointment_repo = AppointmentRepository()
    waitlist_repo = WaitlistRepository()

    return ClinicService(
        doctor_repo,
        patient_repo,
        appointment_repo,
        waitlist_repo
    )

def test_entrar_na_fila_com_sucesso():
    service = create_service()

    service.schedule_appointment(10, 1, "09:00")

    result = service.join_waitlist(40, 1, "09:00")

    assert result is True
    assert service.waitlist_repository.has_entry(40, 1, "09:00")


def test_nao_entra_na_fila_se_slot_livre():
    service = create_service()

    result = service.join_waitlist(40, 1, "09:00")

    assert result is False


def test_nao_entra_na_fila_se_ja_existe():
    service = create_service()

    service.schedule_appointment(10, 1, "09:00")
    service.join_waitlist(40, 1, "09:00")

    result = service.join_waitlist(40, 1, "09:00")

    assert result is False


def test_nao_entra_na_fila_paciente_bloqueado():
    service = create_service()

    service.schedule_appointment(10, 1, "09:00")

    result = service.join_waitlist(20, 1, "09:00")

    assert result is False