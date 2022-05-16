from faker import Faker
from src.infra.config import DBConnectionHandler
from src.infra.repo.person_repository import PersonRepository
from src.infra.entities import PersonsModel

faker = Faker()
person_repository = PersonRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_person():
    """ Should Insert Person """

    name = faker.name()
    engine = db_connection_handler.get_engine()

    # SQL Commands
    new_person = person_repository.insert_person(name)
    query_person = engine.execute(
        f"SELECT * FROM persons WHERE id='{new_person.id}';"
    ).fetchone()

    engine.execute(f"DELETE FROM persons WHERE id='{new_person.id}'")

    assert new_person.id == query_person.id
    assert new_person.name == query_person.name


def test_select_person():
    """ Should select a person in Persons table and compare it """

    person_id = faker.random_number(digits=5)
    name = faker.name()
    data = PersonsModel(id=person_id, name=name)

    engine = db_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO persons (id, name) VALUES ('{person_id}','{name}');"
    )

    query_person1 = person_repository.select_person(person_id=person_id)
    query_person2 = person_repository.select_person(name=name)
    query_person3 = person_repository.select_person(person_id=person_id, name=name)

    assert data in query_person1
    assert data in query_person2
    assert data in query_person3

    engine.execute(f"DELETE FROM persons WHERE id='{person_id}';")
