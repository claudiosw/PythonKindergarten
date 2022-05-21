from typing import List
from src.domain.models import ClassRooms
from tests.domain import mock_classrooms


class ClassRoomRepositorySpy:
    """ Spy to ClassRoom Repository """

    def __init__(self):
        self.insert_classroom_params = {}
        self.select_classroom_params = {}

    def insert_classroom(self, name: str, teacher_id: int) -> ClassRooms:
        """ Spy to all the attributes """

        self.insert_classroom_params["name"] = name
        self.insert_classroom_params["teacher_id"] = teacher_id

        return mock_classrooms()

    def select_classroom(self, classroom_id: int = None, name: str = None) -> List[ClassRooms]:
        """ Spy to all the attributes """

        self.select_classroom_params["classroom_id"] = classroom_id
        self.select_classroom_params["name"] = name

        return [mock_classrooms()]
