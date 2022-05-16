from typing import List
from src.domain.models import Persons
from tests.domain import mock_persons


class PersonRepositorySpy:
    """ Spy to Person Repository """

    def __init__(self):
        self.insert_person_params = {}
        self.select_person_params = {}

    def insert_person(self, name: str) -> Persons:
        """ Spy to all the attributes """

        self.insert_person_params["name"] = name

        return mock_persons()

    def select_person(self, person_id: int = None, name: str = None) -> List[Persons]:
        """ Spy to all the attributes """

        self.select_person_params["person_id"] = person_id
        self.select_person_params["name"] = name

        return [mock_persons()]
