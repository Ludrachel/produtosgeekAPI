from sqlmodel import create_engine, SQLModel # type: ignore

def get_engine():
    url = 'sqlite:///database.db'
    return create_engine(url, echo=True)

def sync_database(engine):
    SQLModel.metadata.create_all(engine)