from src.patient_repository import PatientRepository


def test_exists_returns_true_for_known_patient():
    repository = PatientRepository()
    assert repository.exists(10) is True


def test_exists_returns_false_for_unknown_patient():
    repository = PatientRepository()
    assert repository.exists(999) is False


def test_is_blocked_returns_true_for_blocked_patient():
    repository = PatientRepository()
    assert repository.is_blocked(20) is True


def test_is_blocked_returns_false_for_regular_patient():
    repository = PatientRepository()
    assert repository.is_blocked(10) is False


def test_has_financial_pending_returns_true_when_patient_has_pending():
    repository = PatientRepository()
    assert repository.has_financial_pending(30) is True


def test_has_financial_pending_returns_false_when_patient_has_no_pending():
    repository = PatientRepository()
    assert repository.has_financial_pending(10) is False
