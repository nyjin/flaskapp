from flaskapp.main import create_app
from flask_script import Manager, prompt_bool
from flaskapp.extensions import db

app = create_app()
manager = Manager(app)


@manager.command
def createdb():
    with app.app_context():
        db.create_all()
        db.session.commit()

@manager.command
def dropdb():
    with app.app_context():
        if prompt_bool("모든 데이터를 삭제 하시겠습니까?"):
            db.drop_all()
            db.session.commit()



if __name__ == "__main__":
    manager.run()
