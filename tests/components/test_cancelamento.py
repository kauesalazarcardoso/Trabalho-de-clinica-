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

def test_cancelamento_simples():
    service = create_service()

    service.schedule_appointment(10, 1, "09:00")

    result = service.cancel_appointment(10, 1, "09:00")

    repo = service.appointment_repository

    assert result is True
    assert not repo.has_appointment(10, 1, "09:00")


def test_cancelamento_agenda_proximo_da_fila():
    service = create_service()

    service.schedule_appointment(10, 1, "09:00")
    service.join_waitlist(40, 1, "09:00")

    service.cancel_appointment(10, 1, "09:00")

    repo = service.appointment_repository
    waitlist = service.waitlist_repository

    assert repo.has_appointment(40, 1, "09:00")
    assert not waitlist.has_entry(40, 1, "09:00")


def test_cancelamento_sem_consulta():
    service = create_service()

    result = service.cancel_appointment(10, 1, "09:00")

    assert result is False


def test_cancelamento_dados_invalidos():
    service = create_service()

    with pytest.raises(ValueError):
        service.cancel_appointment(None, 1, "09:00")
        