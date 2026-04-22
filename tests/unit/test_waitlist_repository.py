import pytest
from src.waitlist_repository import WaitlistRepository


def test_add_entry_registers_waitlist_entry():
    repository = WaitlistRepository()
    repository.add_entry(40, 1, "2026-06-10 09:00")
    assert repository.has_entry(40, 1, "2026-06-10 09:00") is True


def test_add_entry_raises_for_duplicate_entry():
    repository = WaitlistRepository()
    repository.add_entry(40, 1, "2026-06-10 09:00")

    with pytest.raises(ValueError, match="Waitlist entry already exists"):
        repository.add_entry(40, 1, "2026-06-10 09:00")


def test_has_any_entry_returns_true_when_slot_has_waitlist():
    repository = WaitlistRepository()
    repository.add_entry(40, 1, "2026-06-10 09:00")
    assert repository.has_any_entry(1, "2026-06-10 09:00") is True


def test_next_patient_returns_first_patient_in_queue():
    repository = WaitlistRepository()
    repository.add_entry(40, 1, "2026-06-10 09:00")
    repository.add_entry(50, 1, "2026-06-10 09:00")
    assert repository.next_patient(1, "2026-06-10 09:00") == 40


def test_remove_entry_removes_existing_waitlist_entry():
    repository = WaitlistRepository()
    repository.add_entry(40, 1, "2026-06-10 09:00")
    repository.remove_entry(40, 1, "2026-06-10 09:00")
    assert repository.has_entry(40, 1, "2026-06-10 09:00") is False
