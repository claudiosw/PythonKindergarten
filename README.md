# Preparing / Installing

### Clone the PythonKindergarten repository
```
git clone https://github.com/claudiosw/PythonKindergarten.git
```

### Access the project directory:
```
cd PythonKindergarten
```

### Create the virtual environment:
```
python -m venv venv

```

### Run the virtual environment:
```
venv\Scripts\activate

```

### Install the required Python packages:
```
pip install -r requirements.txt
```

### Create the database and the database structure:
```
python
>>> from src.infra.config import *
>>> from src.infra.entities import *
>>> db_conn = DBConnectionHandler()
>>> engine = db_conn.get_engine()
>>> Base.metadata.create_all(engine)
```

# Run / Use
## Creating a person (teacher, student or parents)
```
python
>>> from src.data.register_person import RegisterPerson
>>> from src.infra.repo.person_repository import PersonRepository 
>>> person_repository = PersonRepository() 
>>> register_person = RegisterPerson(person_repository) 
>>> response = register_person.register("Teacher Richard")
>>> response
{'Success': True, 'Data': Persons(id=51689, name='Teacher Richard')}
```
## Creating a classroom
```
>>> from src.data.find_person.find_person import FindPerson
>>> find_person = FindPerson(PersonRepository())
>>> from src.data.register_classroom import RegisterClassRoom
>>> from src.infra.repo.classroom_repository import ClassRoomRepository
>>> from src.data.register_classroom import RegisterClassRoom 
>>> classroom_repository = ClassRoomRepository()
>>> register_classroom = RegisterClassRoom(classroom_repository, find_person)
>>> response_classroom = register_classroom.register("Richard classroom", {'id': response['Data'].id})
>>> response_classroom
{'Success': True, 'Data': ClassRooms(id=2, name='Richard classroom', teacher_id=51689)}
```

# Tests
To run the tests, just execute:
```
pytest
```