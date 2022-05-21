from typing import Dict
from abc import ABC, abstractclassmethod
from src.domain.models import ClassRooms


class RegisterClassRoomInterface(ABC):
    """ Interface to RegisterClassRoom use case """

    @abstractclassmethod
    def register(cls, name: str) -> Dict[bool, ClassRooms]:
        """ Case """

        raise Exception("Should implement method: register")
