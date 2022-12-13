from flask import Blueprint,request,jsonify

class AbstractRoute:
    def __init__(self,document_name,odm):
        self.document_name = document_name
        self.odm = odm
        self.blueprint = Blueprint(
            self.document_name,
            __name__,
            url_prefix=f"/api/{self.document_name}"
        )

    def inject_app(self,app):
        @self.blueprint.route("/ping")
        def hello_world():
            return f"<p>Hello {self.document_name}!</p>"

        @self.blueprint.route(f"/create",methods=["POST"])
        def create():
            objectId = self.odm.create(self.document_name,request.form.to_dict())
            return request.form

        @self.blueprint.route("/read")
        def read():
            results = self.odm.getByQuery(self.document_name,{})
            return self.odm.parse_json(results)

        @self.blueprint.route("/update",methods=["PUT"])
        def update():
            self.odm.updateOne(self.document_name,request.json['filter'],request.json["update_data"])
            return True

        # Register the blueprint in injected Flask app
        app.register_blueprint(self.blueprint)    

class ModularRoute:
    def __init__(self,schema,odm):
        self.schema = schema
        self.odm = odm
        self.document_name = schema["model_name_plural"]
        self.blueprint = Blueprint(
            self.document_name,
            __name__,
            url_prefix=f"/api/{self.document_name}"
            )
    
    def inject_app(self,app):
        @self.blueprint.route("/ping")
        def hello_world():
            return f"<p>Hello {self.document_name}!</p>"

        @self.blueprint.route(f"/create",methods=["POST"])
        def create():
            objectId = self.odm.create(self.document_name,request.form.to_dict())
            return request.form

        @self.blueprint.route("/read")
        def read():
            results = self.odm.getByQuery(self.document_name,{})
            return self.odm.parse_json(results)

        @self.blueprint.route("/update",methods=["PUT"])
        def update():
            self.odm.updateOne(self.document_name,request.json['filter'],request.json["update_data"])
            return True

        app.register_blueprint(self.blueprint)
        
class SchemaRoute(AbstractRoute):
    def __init__(self,odm):
        self.modular_routers = {}
        AbstractRoute.__init__(self,"schema",odm)

    def addModularRoute(self,schema):
        modular_route = ModularRoute(schema,self.odm)