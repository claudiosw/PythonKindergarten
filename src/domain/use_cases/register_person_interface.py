from typing import Dict
from abc import ABC, abstractclassmethod
from src.domain.models import Persons


class RegisterPersonInterface(ABC):
    """ Interface to RegisterPerson use case """

    @abstractclassmethod
    def register(cls, name: str) -> Dict[bool, Persons]:
        """ Case """

        raise Exception("Should implement method: register")
