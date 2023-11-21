from fastapi import APIRouter
from config.db import conn
from models.admin import admins
from schemas.admin import Admin
from fastapi.responses import JSONResponse

admin = APIRouter()

@admin.get('/admin/list', tags=["admin"], response_model=list[Admin], description="Get all Admins")
def get_all_admins():
    admin_rows = conn.execute(admins.select()).fetchall()
    admin_dicts = [row._asdict() for row in admin_rows]
    return JSONResponse(content=admin_dicts)


@admin.post('/admin/create', tags=["admin"], response_model=Admin, description="Create a new Admin")
def create_admin(admin: Admin):
    try:
        new_admin = {"name": admin.name, "lastNameFather": admin.lastNameFather, "email": admin.email, "password": admin.password, "admin": admin.admin}
        result = conn.execute(admins.insert().values(new_admin))
        conn.commit()
        created_admin_id = result.lastrowid
        created_admin = {**new_admin, "id": created_admin_id}
        return created_admin
    except Exception as e:
        print("Error:", e)
        raise


@admin.delete('/admin/delete/{email}', tags=["admin"], description="Delete admin by email")
def delete_admin(email: str):
    try:
        conn.execute(admins.delete().where(admins.c.email == email))
        conn.commit()
        return {"message": "Admin deleted"}
    except Exception as e:
        print("Error:", e)
        raise


@admin.put('/admin/update/{email}', tags=["admin"], response_model=Admin, description="Update admin by email")
def update_admin(email: str, admin: Admin):
    try:
        conn.execute(
            admins.update().values(name=admin.name, lastNameFather=admin.lastNameFather, email=admin.email, password=admin.password).where(
                admin.c.email == email
            )
        )
        conn.commit()
        return admin
    except Exception as e:
        print("Error:", e)
        raise

# logearse
@admin.post('/admin/login', tags=["admin"], response_model=Admin, description="Login admin")
def login_admin(admin: Admin):
    try:
        admin_rows = conn.execute(admins.select().where(admins.c.email == admin.email)).fetchall()
        admin_dicts = [row._asdict() for row in admin_rows]
        return JSONResponse(content=admin_dicts)
    except Exception as e:
        print("Error:", e)
        raise

