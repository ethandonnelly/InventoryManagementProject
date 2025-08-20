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
        super().__init__()
        self.username = username
        self.password = password

    def __str__(self):
        return f"{self.username}/{self.password}"

    @staticmethod
    def hash_password(key):
        return ord(key)

    @staticmethod
    def validate_new_username_and_password(username, password):
        if 4 <= len(username) <= 30:
            if 7 <= len(password) <= 30:
                hashed_password = User.hash_password(password)
                new_user = User(username=username, password=hashed_password)
                session.add(new_user)
                return True
            else:
                return "Password needs to be between 7 and 30 characters"
        else:
            return "Username needs to be 4 and 30 characters"

    @staticmethod
    def validate_existing_username_and_password(username, password):
        if session.query(User).filter(User.username == username, User.password == password):
            return True, username
        else:
            return "Incorrect Username or Password"





