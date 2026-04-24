import pytest
from src.clinic_service import ClinicService
from src.appointment_repository import AppointmentRepository
from src.doctor_repository import DoctorRepository
from src.patient_repository import PatientRepository
from src.waitlist_repository import WaitlistRepository


def create_service():
    return ClinicService(
        DoctorRepository(),
        PatientRepository(),
        AppointmentRepository(),
        WaitlistRepository(),
    )


def test_agendamento_com_sucesso():
    service = create_service()

    result = service.schedule_appointment(10, 1, "2026-06-10 09:00")

    assert result is True


def test_nao_agenda_paciente_inexistente():
    service = create_service()

    result = service.schedule_appointment(999, 1, "2026-06-10 09:00")

    assert result is False


def test_nao_agenda_medico_inexistente():
    service = create_service()

    result = service.schedule_appointment(10, 999, "2026-06-10 09:00")

    assert result is False


def test_nao_agenda_paciente_bloqueado():
    service = create_service()

    result = service.schedule_appointment(20, 1, "2026-06-10 09:00")

    assert result is False


def test_nao_agenda_paciente_com_pendencia():
    service = create_service()

    result = service.schedule_appointment(30, 1, "2026-06-10 09:00")

    assert result is False


def test_nao_agenda_mais_de_duas_consultas():
    service = create_service()

    service.schedule_appointment(10, 1, "09:00")
    service.schedule_appointment(10, 2, "10:00")

    result = service.schedule_appointment(10, 3, "11:00")

    assert result is False


def test_nao_agenda_slot_ocupado():
    service = create_service()

    service.schedule_appointment(10, 1, "09:00")

    result = service.schedule_appointment(40, 1, "09:00")

    assert result is False

def test_nao_agenda_id_negativo():
    service = create_service()