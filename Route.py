from flask import Blueprint,request,jsonify

"""
Abstract Route is about managing schema for document entries
"""
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

        @self.blueprint.route("/list")
        def get_list():
            return self.odm.list_schema()

        @self.blueprint.route(f"/create",methods=["POST"])
        def create():
            objectId = self.odm.create_schema(request.json)
            return self.odm.parse_json(request.json)

        @self.blueprint.route("/read")
        def read():
            results = self.odm.getAll(self.document_name)
            return self.odm.parse_json(results)

        @self.blueprint.route("/update",methods=["PUT"])
        def update():
            try:
                self.odm.updateOne(self.document_name,request.json['filter'],request.json["update_data"])
                return {"message":[
                    "update succeed"
                ]}
            except Exception as e:
                return {"message":[
                    "update fail"
                ]}

        # Register the blueprint in injected Flask app
        app.register_blueprint(self.blueprint)    

"""
Modular Route mainly for handling entries related to schema
"""
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
        
        @self.blueprint.route(f"/api/count/<document_name>",methods=["GET"])
        def count(document_name):
            count = self.odm.count_entries(document_name)
            return {"count":count,"schema":document_name}

        @self.blueprint.route(f"/api/create/<document_name>",methods=["POST"])
        def create(document_name):
            objectId = self.odm.create(document_name,request.form.to_dict())
            return request.form

        @self.blueprint.route(f"/api/read/<document_name>")
        def read(document_name):
            results = self.odm.getByQuery(document_name,{})
            return self.odm.parse_json(results)

        @self.blueprint.route(f"/api/update_one/<document_name>",methods=["PUT"])
        def updateOne(document_name):
            try:
                self.odm.updateOne(document_name,request.json['filter'],request.json["update_data"])
                return {"message":[
                    "update succeed"
                ]}
            except Exception as e:
                print(e)
                return {"message":[
                        "update fails"
                    ]}

        @self.blueprint.route(f"/api/delete_one/<document_name>",methods=['POST'])
        def deleteOne(document_name):
            try:
                self.odm.deleteOne(document_name,request.json['filter'])
                print("Not here")
                return {"message":[
                    "delete succeed"
                ]}
            except Exception as e:
                print(e)
                return {"message":[
                        "delete fails"
                    ]}

        # Register the blueprint in injected Flask app
        app.register_blueprint(self.blueprint)

        
class SchemaRoute(AbstractRoute):
    def __init__(self,odm):
        self.modular_routers = {}
        AbstractRoute.__init__(self,"schema_collection",odm)

    def addModularRoute(self,schema):
        modular_route = ModularRoute(schema,self.odm)
        modular_route.inject_app(self.injected_app)
