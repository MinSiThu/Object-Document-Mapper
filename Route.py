from flask import request,jsonify

class Route:
    def __init__(self,schema,odm):
        self.schema = schema
        self.odm = odm
        self.document_name = schema["model_name_plural"]
    
    def inject_app(self,app):
        @app.route(f"/api/{self.document_name}/ping")
        def hello_world():
            return f"<p>Hello {self.document_name}!</p>"

        @app.route(f"/api/{self.document_name}/create",methods=["POST"])
        def create():
            objectId = self.odm.create(self.document_name,request.form.to_dict())
            return request.form

        @app.route(f"/api/{self.document_name}/read")
        def read():
            results = self.odm.getByQuery(self.document_name,{})
            return self.odm.parse_json(results)

        @app.route(f"/api/{self.document_name}/update",methods=["PUT"])
        def update():
            self.odm.updateOne(self.document_name,request.json['filter'],request.json["update_data"])
            return True