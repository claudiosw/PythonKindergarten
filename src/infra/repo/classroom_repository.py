from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.data.interfaces import ClassRoomRepositoryInterface
from src.domain.models import ClassRooms
from src.infra.config import DBConnectionHandler
from src.infra.entities import ClassRoomsModel


class ClassRoomRepository(ClassRoomRepositoryInterface):
    """ Class to manage ClassRoom Repository """

    @classmethod
    def insert_classroom(cls, name: str, teacher_id: int) -> ClassRooms:
        """insert data in classroom entity
        :param  - name: classroom name
                - teacher_id: id of the teacher
        :return - tuple with new classroom inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_classroom = ClassRoomsModel(name=name, teacher_id=teacher_id)
                db_connection.session.add(new_classroom)
                db_connection.session.commit()

                return ClassRooms(
                    id=new_classroom.id, name=new_classroom.name, teacher_id=new_classroom.teacher_id
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_classroom(cls, classroom_id: int = None, name: str = None) -> List[ClassRooms]:
        """
        Select data in classroom entity by id and/or name
        :param - classroom_id: Id of the registry
               - name: ClassRoom name
        :return - List with ClassRooms selected
        """

        try:
            query_data = None

            if classroom_id and not name:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(ClassRoomsModel)
                        .filter_by(id=classroom_id)
                        .one()
                    )
                    query_data = [data]

            elif not classroom_id and name:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(ClassRoomsModel)
                        .filter_by(name=name)
                        .one()
                    )
                    query_data = [data]

            elif classroom_id and name:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(ClassRoomsModel)
                        .filter_by(id=classroom_id, name=name)
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
