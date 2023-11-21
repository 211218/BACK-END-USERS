from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import meta, engine

teachers = Table("teachers", meta,
        Column("id", Integer, primary_key=True),
        Column("name", String(255)),
        Column("lastNameFather", String(255)),
        Column("email", String(255)),
        Column("password", String(255)),
        Column("teacher", Boolean, default=False)
        )

meta.create_all(engine) 