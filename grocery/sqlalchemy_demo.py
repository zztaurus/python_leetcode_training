

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def demo():
    engine = create_engine('sqlite:///grocery.sqlite')
    with sessionmaker(engine) as session:
        session.add_all(["asdfasdf"])
        session.commit()
