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

class GenerateHRD(MethodResource,Resource):
    @doc(description="Renting_in_a_Mall_Drafting_A4",tags=['Renting_in_a_Mall_Drafting_A4'])
    @use_kwargs(schema.HRDRequest,location=('json'))
    @marshal_with(schema.APIResponse)
    def post(self ,**kwargs):
         try:
            print("generateHRD")
            city=kwargs['city']
            day_montha=kwargs['day_montha']
            year=kwargs['year']
            lessor_list=kwargs['lessor_list']
            leasee_list=kwargs['leasee_list']
            #lessorname=kwargs['lessorname']
            #lessorfname=kwargs['lessorfname']
            address1=kwargs['address1']
            #lesseename=kwargs['lesseename']
            #lesseefname=kwargs['lesseefname']
            address2=kwargs['address2']
            leasepropertyaddress=kwargs['leasepropertyaddress']
            leasepropertyarea=kwargs['leasepropertyarea']
            leaseterm=kwargs['leaseterm']
            leasedeedstartdate=kwargs['leasedeedstartdate']
            leasedeedsigndate=kwargs['leasedeedsigndate']
            leaseamount=kwargs['leaseamount']
            monthlypaymentdate=kwargs['monthlypaymentdate']
            twomonths=kwargs['twomonths']
            onemonth=kwargs['onemonth']
            #lessoraddressline1=kwargs['lessoraddressline1']
            #lesseeaddressline1=kwargs['lesseeaddressline1']
            #lessoraddressline2=kwargs['lessoraddressline2']
            #lesseeaddressline2=kwargs['lesseeaddressline2']
            #lessorcitystatepincode=kwargs['lessorcitystatepincode']
            #lesseecitystatepincode=kwargs['lesseecitystatepincode']
            witness1name=kwargs['witness1name']
            witness2name=kwargs['witness2name']
            witness1address=kwargs['witness1address']
            witness2address=kwargs['witness2address']
            db_connection={
               'driver': 'json',
               'data_file': os.path.join(RESOURCES_DIR, 'lessor.json')
            
               }

            )
            pyreportjasper.process_report()
            output_file = output_file + '.html'
            if os.path.isfile(output_file):
               print('Report generated successfully!')
          
            return APIResponse().dump(dict(message="Report generated successfully")), 200
         except Exception as e:
            print(str(e))
            return APIResponse().dump(dict(message="not generated")), 404
api.add_resource(GenerateHRD,'/generateHRD')        
docs.register(GenerateHRD)


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

            
