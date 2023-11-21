from fastapi import APIRouter
from config.db import conn
from models.teacher import teachers
from schemas.teacher import Teacher
from fastapi.responses import JSONResponse

teacher = APIRouter()

@teacher.get('/teacher/list', tags=["teacher"], response_model=list[Teacher], description="Get all Teachers")
def get_all_teachers():
    teacher_rows = conn.execute(teachers.select()).fetchall()
    teacher_dicts = [row._asdict() for row in teacher_rows]
    return JSONResponse(content=teacher_dicts)

@teacher.post('/teacher/create', tags=["teacher"], response_model=Teacher, description="Create a new Teacher")
def create_teacher(teacher: Teacher):
    try:
        new_teacher = {"name": teacher.name, "lastNameFather": teacher.lastNameFather, "email": teacher.email, "password": teacher.password, "teacher": teacher.teacher}
        result = conn.execute(teachers.insert().values(new_teacher))
        conn.commit()
        created_teacher_id = result.lastrowid
        created_teacher = {**new_teacher, "id": created_teacher_id}
        return created_teacher
    except Exception as e:
        print("Error:", e)
        raise

@teacher.delete('/teacher/delete/{email}', tags=["teacher"], description="Delete teacher by email")
def delete_teacher(email: str):
    try:
        conn.execute(teachers.delete().where(teachers.c.email == email))
        conn.commit()
        return {"message": "Teacher deleted"}
    except Exception as e:
        print("Error:", e)
        raise

@teacher.put('/teacher/update/{email}', tags=["teacher"], response_model=Teacher, description="Update teacher by email")
def update_teacher(email: str, teacher: Teacher):
    try:
        conn.execute(
            teachers.update().values(name=teacher.name, lastNameFather=teacher.lastNameFather, email=teacher.email, password=teacher.password).where(
                teacher.c.email == email
            )
        )
        conn.commit()
        return teacher
    except Exception as e:
        print("Error:", e)
        raise

# logearse
@teacher.post('/teacher/login', tags=["teacher"], response_model=Teacher, description="Login teacher")
def login_teacher(teacher: Teacher):
    try:
        teacher_rows = conn.execute(teachers.select().where(teachers.c.email == teacher.email)).fetchall()
        teacher_dicts = [row._asdict() for row in teacher_rows]
        return JSONResponse(content=teacher_dicts)
    except Exception as e:
        print("Error:", e)
        raise