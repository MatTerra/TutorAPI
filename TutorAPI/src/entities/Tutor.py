from dataclasses import dataclass, field

from nova_api.entity import Entity


@dataclass
class Tutor(Entity):
    first_name: str = field(default="", metadata={"type": "VARCHAR(40)",
                                                  "default": "NOT NULL"})
    last_name: str = field(default="", metadata={"type": "VARCHAR(40)",
                                                  "default": "NOT NULL"})
    phone_number: str = field(default=None, metadata={"type": "VARCHAR(13)"})
    email: str = field(default=None, metadata={"type": "VARCHAR(13)"})

    def __post_init__(self):
        super(Tutor, self).__post_init__()

        if not Tutor.__is_valid_name(self.first_name):
            raise ValueError("Invalid First Name")

        if not Tutor.__is_valid_name(self.last_name):
            raise ValueError("Invalid Last Name")

        if self.phone_number is not None \
                and not Tutor.__is_valid_phone(self.phone_number):
            raise ValueError("Invalid Phone Number")

    @classmethod
    def __is_valid_name(cls, name: str):
        if not isinstance(name, str) or not name:
            return False
        return 2 <= len(name) <= 40 and name.replace(" ", "").isalpha()

    @classmethod
    def __is_valid_phone(cls, phone: str):
        if not isinstance(phone, str) or not phone:
            return False
        return 10 <= len(phone) <= 11 and phone.isnumeric()