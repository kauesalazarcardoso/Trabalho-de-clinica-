from src.doctor_repository import DoctorRepository


def test_exists_returns_true_for_known_doctor():
    repository = DoctorRepository()
    assert repository.exists(1) is True


def test_exists_returns_false_for_unknown_doctor():
    repository = DoctorRepository()
    assert repository.exists(999) is False
