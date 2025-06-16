from app import app, db

if __name__ == '__main__':
    app.run(debug=True)

from flask_migrate import Migrate

migrate = Migrate(app, db)

