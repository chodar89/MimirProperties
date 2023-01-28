from shared.enums import StrEnum


def test_string_enum():
    class TestEnum(StrEnum):
        TEST = "TEST"

    assert TestEnum.TEST == "TEST"
    assert TestEnum.TEST.value == "TEST"
    assert str(TestEnum.TEST) == "TEST"
    assert type(TestEnum.TEST) == TestEnum
    assert list(TestEnum) == ["TEST"]
