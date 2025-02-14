from fastapi.testclient import TestClient
<<<<<<< HEAD
=======

>>>>>>> 1bad0e1c27fbb4bca60ceb33189d127d8eaabc4f
from main import app

client = TestClient(app, base_url="http://test/api/v1")
