from app import *
from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with,doc,use_kwargs



class GenerateSDD(MethodResource,Resource):
    @doc(description="Sale Deed Drafting",tags=['Sale Deed Drafting API'])
    @use_kwargs(schema.SDDRequest,location=('json'))
    @marshal_with(schema.APIResponse)
    def post(self ,**kwargs):
         try:
            print("generateSDD")
            parameters=kwargs  
            db_conn=utility.getDbConnection("sellorpurchaser.json","sellers","purchasers",parameters['sellers'],parameters['purchasers'])
            del parameters['sellers']
            del parameters['purchasers']
            utility.generateReport("Sale_Deed_Drafting.jrxml","Sale_Deed_Drafting",parameters,db_conn) 
            return schema.APIResponse().dump(dict(message="Report generated successfully")), 200
         except Exception as e:
            print(str(e))
            return schema.APIResponse().dump(dict(message="not generated")), 404
        
api.add_resource(GenerateSDD,'/generateSDD')        
docs.register(GenerateSDD)

class GeneratePSR(MethodResource, Resource):
    @doc(description="Parking space rental Deed Drafting", tags=['Parking space rental Deed Drafting API'])
    @use_kwargs(schema.PSRRequest, location=('json'))
    @marshal_with(schema.APIResponse)
    def post(self, **kwargs):
        try:
            print("generatePSR")
            parameters=kwargs  
            db_conn=""
            utility.generateReport("Parking_space_rental_Deed_Drafting.jrxml","Parking_space_rental_Deed_Drafting",parameters,db_conn) 
            return schema.APIResponse().dump(dict(message="Report generated successfully")), 200
        except Exception as e:
            print(str(e))
            return schema.APIResponse().dump(dict(message="not generated")), 404
        
api.add_resource(GeneratePSR,'/generatePSR')        
docs.register(GeneratePSR)

class GenerateOSAD(MethodResource,Resource):
    @doc(description="Office sharing  Drafting",tags=['Office sharing  Drafting API'])
    @use_kwargs(schema.OSADRequest,location=('json'))
    @marshal_with(schema.APIResponse)
    def post(self ,**kwargs):
         try:
            print("generateSDD")
            parameters=kwargs  
            db_conn=""
            utility.generateReport("Office_Sharing_Agreement_Drafting.jrxml","Office_Sharing_Agreement_Drafting",parameters,db_conn) 
            return schema.APIResponse().dump(dict(message="Report generated successfully")), 200
         except Exception as e:
            print(str(e))
            return schema.APIResponse().dump(dict(message="not generated")), 404
        
api.add_resource(GenerateOSAD,'/generateOSAD')        
docs.register(GenerateOSAD)

            