from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, mapped_column, Mapped, sessionmaker, relationship

database_url = ""
engine = create_engine(database_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class AbstractBaseClass(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


class User(AbstractBaseClass):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f"{self.username}/{self.password}"

    @staticmethod
    def choose_username():
        pass

    @staticmethod
    def choose_password():
        pass

    @staticmethod
    def hash_password(key):
        return ord(key)

    @staticmethod
    def create_account():
        pass

    @staticmethod
    def login():
        pass