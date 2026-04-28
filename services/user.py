from config.db import conn
from models.user import users
from schemas.user import  UserCreate ,UserUpdate

def get_users():
    return conn.execute(users.select()).fetchall()

def get_user_by_id(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()

def create_user(user: UserCreate):
    conn.execute(users.insert().values(
        name=user.name,
        email=user.email,
        password=user.password
    ))
    conn.commit()  # ← faltaba guardar
    return get_users()

def update_user(id: int, user: UserUpdate):
    conn.execute(
        users.update()          # ← update() sin argumentos
        .values(                # ← los valores van en .values()
            name=user.name,
            email=user.email,
            password=user.password
        )
        .where(users.c.id == id)  # ← where va al final
    )
    conn.commit()  # ← faltaba guardar
    return get_users()

def delete_user(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    conn.commit()  # ← faltaba guardar
    return get_users()