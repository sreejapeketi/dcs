from app import application
from flask import jsonify,Response, session,request
from app import *
from marshmallow import Schema, fields
from flask_restful import Resource, Api
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with,doc,use_kwargs

import json
import os
from pyreportjasper import PyReportJasper


RESOURCES_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'resources')
REPORTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports')

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
            username=parameters['username']
            password=parameters['password']  
            del parameters['username']
            del parameters['password']
            utility.generateReport("Sale_Deed_Drafting.jrxml","Sale_Deed_Drafting",parameters,db_conn,username,password) 
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

            json_file = os.path.join(RESOURCES_DIR, 'lessor.json')
            f = open(json_file, "w")
            f.write("{ \"lessor_list\" : "+json.dumps(lessor_list)+", \"leasee_list\" :"+json.dumps(leasee_list)+"}")
            f.close()

            input_file = os.path.join(REPORTS_DIR, 'Renting_in_a_Mall_Drafting_A4.jrxml')
            output_file = os.path.join(REPORTS_DIR, 'Renting_in_a_Mall_Drafting_A4')
            pyreportjasper = PyReportJasper()
            pyreportjasper.config(
            input_file,
            output_file,
            output_formats=["html"],
            parameters={
               "[City]":city,
               "[DayMonth]":day_montha,
               "[Year]":year,
               #"[Lessor Name]":lessorname,
               #"[Lessor&apos;s Father Name]":lessorfname,
               "[Address1]":address1,
               #"[Lessee Name]":lesseename,
               #"[Lessee’s Father Name]":lesseefname,
               "[Address2]":address2,
               "[Lease Property Address]":leasepropertyaddress,
               "[Lease Property Area]":leasepropertyarea,
               "[Lease Term in Months or Years]":leaseterm,
               "[Lease Deed Start Date]":leasedeedstartdate,
               "[Lease Deed Signing Date]":leasedeedsigndate,
               "[Lease Amount Per Month]":leaseamount,
               "[Date of Monthly Payment]":monthlypaymentdate,
               "[two months]":twomonths,
               "[one month]":onemonth,
               #"Lessor Address Line 1":lessoraddressline1,
               #"Lessee Address Line 1":lesseeaddressline2,
               #"Lessor Address Line 2":lessoraddressline2,
               #"Lessee Address Line 2":lesseeaddressline2,
               #"[City, State Pincode (Lessor)]":lessorcitystatepincode,
               #"[City, State, Pincode (Lessee)]":lesseecitystatepincode,
               "Witness 1 Name":witness1name,
               "Witness 2 Name":witness2name,
               "Witness 1 Address":witness1address,
               "Witness 2 Address":witness2address,
               },
                
               db_connection={
               'driver': 'json',
               'data_file': os.path.join(RESOURCES_DIR, 'lessor.json')
            
               }

            )

            parameters={
               "[City]":city,
               "[DayMonth]":day_montha,
               "[Year]":year,
               #"[Lessor Name]":lessorname,
               #"[Lessor&apos;s Father Name]":lessorfname,
               "[Address1]":address1,
               #"[Lessee Name]":lesseename,
               #"[Lessee’s Father Name]":lesseefname,
               "[Address2]":address2,
               "[Lease Property Address]":leasepropertyaddress,
               "[Lease Property Area]":leasepropertyarea,
               "[Lease Term in Months or Years]":leaseterm,
               "[Lease Deed Start Date]":leasedeedstartdate,
               "[Lease Deed Signing Date]":leasedeedsigndate,
               "[Lease Amount Per Month]":leaseamount,
               "[Date of Monthly Payment]":monthlypaymentdate,
               "[two months]":twomonths,
               "[one month]":onemonth,
               #"Lessor Address Line 1":lessoraddressline1,
               #"Lessee Address Line 1":lesseeaddressline2,
               #"Lessor Address Line 2":lessoraddressline2,
               #"Lessee Address Line 2":lesseeaddressline2,
               #"[City, State Pincode (Lessor)]":lessorcitystatepincode,
               #"[City, State, Pincode (Lessee)]":lesseecitystatepincode,
               "Witness 1 Name":witness1name,
               "Witness 2 Name":witness2name,
               "Witness 1 Address":witness1address,
               "Witness 2 Address":witness2address,
               }
                
            db_connection={
               'driver': 'json',
               'data_file': os.path.join(RESOURCES_DIR, 'lessor.json')
            }

            utility.generateReport("Renting_in_a_Mall_Drafting_A4.jrxml","Renting_in_a_Mall_Drafting_A4",parameters,db_connection) 
            return schema.APIResponse().dump(dict(message="Report generated successfully")), 200
         except Exception as e:
            print(str(e))
            return schema.APIResponse().dump(dict(message="not generated")), 404
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
            print("generateOSAD")
            parameters=kwargs  
            db_conn=""
            utility.generateReport("Office_Sharing_Agreement_Drafting.jrxml","Office_Sharing_Agreement_Drafting",parameters,db_conn) 
            return schema.APIResponse().dump(dict(message="Report generated successfully")), 200
         except Exception as e:
            print(str(e))
            return schema.APIResponse().dump(dict(message="not generated")), 404

class GenerateSPA(MethodResource, Resource):
    @doc(description="One And The Same Person Affidavit Drafting", tags=['One And The Same Person Affidavit Drafting API'])
    @use_kwargs(schema.SPARequest, location=('json'))
    @marshal_with(schema.APIResponse)
    def post(self, **kwargs):
        try:
            print("generateSPA")
            parameters=kwargs  
            db_conn=""
            utility.generateReport("One_And_The_Same_Person_Affidavit_Drafting.jrxml","One_And_The_Same_Person_Affidavit_Drafting",parameters,db_conn) 
            return schema.APIResponse().dump(dict(message="Report generated successfully")), 200
        except Exception as e:
            print(str(e))
            return schema.APIResponse().dump(dict(message="not generated")), 404
        
api.add_resource(GenerateSPA,'/generateSPA')        
docs.register(GenerateSPA)

api.add_resource(GenerateOSAD,'/generateOSAD')        
docs.register(GenerateOSAD)

            
