from abc import ABC, abstractmethod
from typing import List
from src.domain.models import ClassRooms


class ClassRoomRepositoryInterface(ABC):
    """ Interface to Pet Repository """

    @abstractmethod
    def insert_classroom(self, name: str, teacher_id: int) -> ClassRooms:
        """ abstractmethod  """

        raise Exception("Method not implemented")

    @abstractmethod
    def select_classroom(self, classroom_id: int = None, name: str = None) -> List[ClassRooms]:
        """ abstractmethod  """

        raise Exception("Method not implemented")
