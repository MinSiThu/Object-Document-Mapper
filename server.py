from flask import Flask
from Route import Route
from schemas import user_schema
from odm.object_document_mapper import ObjectDocumentMapper

odm = ObjectDocumentMapper(
    "mongodb://localhost:27017/",
    "flask_odm_testing"
    )
app = Flask(__name__)

user_router = Route(user_schema,odm)
user_router.inject_app(app)