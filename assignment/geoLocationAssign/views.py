from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
###########################assignment Geo##################################################33
from rest_framework.parsers import JSONParser
import requests
import json
import urllib
from rest_framework.response import Response
from django.http import JsonResponse
import pandas as pd
import xmltodict
import dicttoxml
############################
''' OUTPUTS:{
"address": "# 3582,13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008",
"output_format": "json"
}


{
"address": "# 3582,13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008",
"output_format": "xml"
}'''
###################################
class getAddressDetails(APIView):
    #that can accept POST requests with JSON content
    parser_classes = [JSONParser]
    def post(self, request):
        #to check the output type
        if request.data['output_format']=="json":
            base_url= "https://maps.googleapis.com/maps/api/geocode/json?"
            AUTH_KEY = "" #Key
            parameters = {"address": request.data['address'],"key": AUTH_KEY}
            # urllib.parse.urlencode turns parameters into url
            r = requests.get(f"{base_url}{urllib.parse.urlencode(parameters)}")
            data = json.loads(r.content)
            return Response({"coordinates":data.get("results")[0].get("geometry").get("location"),"address":request.data['address']})
        elif request.data['output_format']=="xml":
            base_url= "https://maps.googleapis.com/maps/api/geocode/xml?"
            AUTH_KEY = "AIzaSyCOD3KvY2DDzEfel-NZ_LKIWXr86EF_EUw"
            parameters = {"address": request.data['address'],"key": AUTH_KEY}
            # urllib.parse.urlencode turns parameters into url
            r = requests.get(f"{base_url}{urllib.parse.urlencode(parameters)}")
            decoded_response = r.content.decode('utf-8')
            #converting the xml content to json
            response_json = json.loads(json.dumps(xmltodict.parse(decoded_response)))
            json_obj={"address":request.data['address'],"coordinates":response_json['GeocodeResponse']['result']['geometry']['location']}
            #converting json to xml using dicttoxml
            xml = dicttoxml.dicttoxml(json_obj)
            return Response(xml)
        else:
            return Response({"result":"Invalid Type"})