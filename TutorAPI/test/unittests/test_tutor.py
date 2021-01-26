from pytest import mark, raises

from entities.tutor import Tutor

INVALID_NAMES = [
        "",
        "a",
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "12",
        "abc12",
        123
    ]

INVALID_PHONES = [
        "9234",
        "a",
        "9999888a",
        "12",
        "abc12",
        123
    ]

VALID_NAMES = [
        "Maria Luiza"
    ]

VALID_PHONES = [
        "61999998888"
    ]


class TestTutor:
    @mark.parametrize("name", INVALID_NAMES)
    def test_tutor_with_invalid_first_name_should_fail(self, name):
        with raises(ValueError) as e:
            Tutor(first_name=name, last_name="Teste")
        assert str(e.value) == "Invalid First Name"

    @mark.parametrize("name", INVALID_NAMES)
    def test_tutor_with_invalid_last_name_should_fail(self, name):
        with raises(ValueError) as e:
            Tutor(first_name="Teste", last_name=name)
        assert str(e.value) == "Invalid Last Name"

    @mark.parametrize("name", VALID_NAMES)
    def test_tutor_with_valid_first_name_and_last_name(self, name):
        tutor = Tutor(first_name=name, last_name=name)
        assert tutor.first_name == name
        assert tutor.last_name == name

    @mark.parametrize("phone", INVALID_PHONES)
    def test_invalid_phone_should_fail(self, phone):
        with raises(ValueError) as e:
            Tutor(first_name="Teste", last_name="Teste", phone_number=phone)
        assert str(e.value) == "Invalid Phone Number"

    @mark.parametrize("phone", VALID_PHONES)
    def test_tutor_with_valid_phone_number(self, phone):
        tutor = Tutor(first_name="Teste", last_name="Teste",
                      phone_number=phone)
        assert tutor.phone_number == phone


