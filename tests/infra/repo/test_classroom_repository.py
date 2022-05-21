from faker import Faker
from src.infra.config import DBConnectionHandler
from src.infra.repo.classroom_repository import ClassRoomRepository
from src.infra.entities import ClassRoomsModel

faker = Faker()
classroom_repository = ClassRoomRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_classroom():
    """ Should Insert ClassRoom """

    name = "Classroom {faker.random_number()}"
    teacher_id = faker.random_number()
    engine = db_connection_handler.get_engine()

    # SQL Commands
    new_classroom = classroom_repository.insert_classroom(name, teacher_id)
    query_classroom = engine.execute(
        f"SELECT * FROM class_rooms WHERE id='{new_classroom.id}';"
    ).fetchone()

    engine.execute(f"DELETE FROM class_rooms WHERE id='{new_classroom.id}'")

    assert new_classroom.id == query_classroom.id
    assert new_classroom.name == query_classroom.name
    assert new_classroom.teacher_id == query_classroom.teacher_id


def test_select_classroom():
    """ Should select a classroom in ClassRooms table and compare it """

    classroom_id = faker.random_number(digits=5)
    name = faker.name()
    teacher_id = faker.random_number()
    data = ClassRoomsModel(id=classroom_id, name=name, teacher_id=teacher_id)

    engine = db_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO class_rooms (id, name, teacher_id) VALUES ('{classroom_id}','{name}', '{teacher_id}');"
    )

    query_classroom1 = classroom_repository.select_classroom(classroom_id=classroom_id)
    query_classroom2 = classroom_repository.select_classroom(name=name)
    query_classroom3 = classroom_repository.select_classroom(classroom_id=classroom_id, name=name)

    assert data in query_classroom1
    assert data in query_classroom2
    assert data in query_classroom3

    engine.execute(f"DELETE FROM class_rooms WHERE id='{classroom_id}';")
