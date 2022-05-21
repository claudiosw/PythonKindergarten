from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.data.interfaces import PersonRepositoryInterface
from src.domain.models import Persons
from src.infra.config import DBConnectionHandler
from src.infra.entities import PersonsModel


class PersonRepository(PersonRepositoryInterface):
    """ Class to manage Person Repository """

    @classmethod
    def insert_person(cls, name: str) -> Persons:
        """insert data in person entity
        :param - name: person name
        :return - tuple with new person inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_person = PersonsModel(name=name)
                db_connection.session.add(new_person)
                db_connection.session.commit()

                return Persons(
                    id=new_person.id, name=new_person.name
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_person(cls, person_id: int = None, name: str = None) -> List[Persons]:
        """
        Select data in person entity by id and/or name
        :param - person_id: Id of the registry
               - name: Person name
        :return - List with Persons selected
        """

        try:
            query_data = None

            if person_id and not name:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PersonsModel)
                        .filter_by(id=person_id)
                        .one()
                    )
                    query_data = [data]

            elif not person_id and name:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PersonsModel)
                        .filter_by(name=name)
                        .one()
                    )
                    query_data = [data]

            elif person_id and name:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PersonsModel)
                        .filter_by(id=person_id, name=name)
                        .one()
                    )
                    query_data = [data]

            return query_data

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

        return None
