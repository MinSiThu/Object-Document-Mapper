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
        self.middlewares = {}

    def inject_app(self,app):
        self.injected_app = app

        @self.blueprint.route("/ping")
        def hello_world():
            return f"<p>Hello {self.document_name}!</p>"

        @self.blueprint.route(f"/create",methods=["POST"])
        def create():
            print(request.json)
            objectId = self.odm.create(self.document_name,request.json)
            return request.json

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
    def __init__(self,odm):
        self.odm = odm
        self.blueprint = Blueprint(
            "modular",
            __name__,
            url_prefix=f"/modular"
        )
    
    def inject_app(self,app):
        @self.blueprint.route(f"/api/ping")
        def hello_world():
            return f"<h3>Hello Modular!</h3>"

        @self.blueprint.route(f"/api/create/<document_name>",methods=["POST"])
        def create(document_name):
            objectId = self.odm.create(document_name,request.form.to_dict())
            return request.form

        @self.blueprint.route(f"/api/read/<document_name>")
        def read(document_name):
            results = self.odm.getByQuery(document_name,{})
            return self.odm.parse_json(results)

        @self.blueprint.route(f"/api/update/<document_name>",methods=["PUT"])
        def update(document_name):
            try:
                self.odm.updateOne(document_name,request.json['filter'],request.json["update_data"])
                return {"message":[
                    "update succeed"
                ]}
            except:
                return {"message":[
                        "update fails"
                    ]}

        # Register the blueprint in injected Flask app
        app.register_blueprint(self.blueprint)

        
class SchemaRoute(AbstractRoute):
    def __init__(self,odm):
        self.modular_routers = {}
        AbstractRoute.__init__(self,"schema",odm)

    def addModularRoute(self,schema):
        modular_route = ModularRoute(schema,self.odm)
        modular_route.inject_app(self.injected_app)
