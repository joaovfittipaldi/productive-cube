from app import environment
from app import worker
from app import create_app
from flask import jsonify

secret_key, user, password, broker = environment.load_ambient_variables()
data = {"user": user, "password": password}

app = create_app(secret_key=secret_key, data=data, database="focus_cube")
# Saved
if __name__ == "__main__":
    worker.start_worker(broker=broker, topic="focuscube/status")
    worker.start_worker(broker=broker, topic="focuscube/comando")
    app.run()
    