# database.py
from   sqlalchemy   import create_engine ,MetaData
from dotenv import load_dotenv
import os
load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))
meta =MetaData()
conn = engine.connect()