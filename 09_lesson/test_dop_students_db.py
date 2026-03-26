from sqlalchemy import create_engine, text

'postgresql://postgres:aA123123@localhost:5432/postgres'


def test_check_connection():
    engine = create_engine(db_connection)
    with engine.connect() as conn:
        result = conn.execute(text("select * from student limit 1")).fetchone()
        print(result)
        assert result is not None


def test_add_student():
    with create_engine(db_connection).connect() as conn:
        conn.execute(text("insert into student(level) values ('Test Level')"))
        conn.commit()

        result = conn.execute(text("select level from student where level = 'Test Level'")).fetchone()
        assert result.level == "Test Level"

        conn.execute(text("delete from student where level = 'Test Level'"))
        conn.commit()


def test_edit():
    with create_engine(db_connection).connect() as conn:
        conn.execute(text("insert into student(education_form) values ('Test Edit')"))
        conn.commit()

        conn.execute(text("update student set subject_id = 2 where education_form = 'Test Edit'"))
        conn.commit()

        updated = conn.execute(text("select subject_id from student where education_form = 'Test Edit'")).fetchone()
        assert updated.subject_id == 2

        conn.execute(text("delete from student where education_form = 'Test Edit'"))
        conn.commit()


def test_delete():
    with create_engine(db_connection).connect() as conn:
        conn.execute(text("insert into student(education_form) values ('For delete')"))
        conn.commit()

        conn.execute(text("delete from student where education_form = 'For delete'"))
        conn.commit()

        deleted = conn.execute(text("select * from student where education_form = 'For delete'")).fetchone()
        assert deleted is None