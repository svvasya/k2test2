from flask import Flask
from k2test.views import k2test_bp

app = Flask(__name__)
app.register_blueprint(k2test_bp)
