# Usando sqlAlchemy para fazer a abstração da conexão com o banco
from sqlalchemy import create_engine, text
from decouple import config


url = config("db_url")
# Echo loga as queries
_engine = create_engine(url, echo=True)


def execute(query: str):
    with (_engine.connect()) as conn:
        statement = text(query)
        transaction = conn.begin()
        conn.execute(statement)
        transaction.commit()
