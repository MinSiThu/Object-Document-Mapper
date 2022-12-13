from flask import Flask
from Route import ModularRoute,SchemaRoute
from schemas import user_schema
from odm.object_document_mapper import ObjectDocumentMapper

odm = ObjectDocumentMapper(
    "mongodb://localhost:27017/",
    "flask_odm_testing"
    )
app = Flask(__name__)

schema_router = SchemaRoute(odm)
schema_router.inject_app(app)