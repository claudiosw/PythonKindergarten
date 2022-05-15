from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Persons


class PersonRepositoryInterface(ABC):
    """ Interface to Pet Repository """

    @abstractmethod
    def insert_person(self, name: str) -> Persons:
        """ abstractmethod  """

        raise Exception("Method not implemented")

    @abstractmethod
    def select_person(self, person_id: int = None, name: str = None) -> List[Persons]:
        """ abstractmethod  """

        raise Exception("Method not implemented")
