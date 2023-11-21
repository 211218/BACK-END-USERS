from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:cxxmigue211218@localhost:3306/api_integrador")

meta = MetaData()

conn = engine.connect()