
from flask_restx import Namespace, Resource
health_ns = Namespace("health", description="Service health checks")
@health_ns.route("")
class Health(Resource):
    def get(self): return {"status":"ok"},200
