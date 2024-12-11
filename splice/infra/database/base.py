from sqlalchemy.orm import declarative_base, registry

Base = declarative_base()


table_registry = registry()
