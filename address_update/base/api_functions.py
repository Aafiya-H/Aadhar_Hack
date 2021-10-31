import requests
import uuid
import json
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

base_url = 'https://stage1.uidai.gov.in/onlineekyc/'

def otp(uid):
    txn_id = str(uuid.uuid4())
    api_url = base_url + 'getOtp/'
    params = {
        "uid":uid,
        "txnId":txn_id
    }
    headers={
    'Content-type':'application/json', 
    'Accept':'application/json'
    }
    r = requests.post(url = api_url, data = json.dumps(params),headers = headers)
    res = json.loads(r.text)
    print(res)
    return {'status':res['status'], 'txnID':txn_id, 'error_code':res['errCode']} 

def auth(uid,otp,txn_id):
    api_url = base_url + 'getAuth/'
    params = {
        "uid":uid,
        "txnId":txn_id,
        "otp":otp
    }
    headers={
    'Content-type':'application/json', 
    'Accept':'application/json'
    }
    r = requests.post(url = api_url, data = json.dumps(params),headers = headers)
    res = json.loads(r.text)
    print(res)
    return {'status':res['status'], 'error_code':res['errCode']} 

def parse_xml(data):
    bs_data = BeautifulSoup(data, "xml")
    b_unique = bs_data.find('Poa')
    print(b_unique.attrs)
    return b_unique.attrs

def eKyc(uid,otp,txn_id):                                              
    api_url = base_url + 'getEkyc/'
    params = {
        "uid":uid,
        "txnId":txn_id,
        "otp":otp
    }
    headers={
    'Content-type':'application/json', 
    'Accept':'application/json'
    }
    r = requests.post(url = api_url, data = json.dumps(params),headers = headers)
    res = json.loads(r.text)
    print(res['status'])
    xml_string = res['eKycString']
    print(xml_string)
    print(res['errCode'])
    address_dict = parse_xml(xml_string),
    aadhar_holder_name = 'Aadhar Holder Name'
    return {'status':res['status'],'error_code':res['errCode'], 'address_dict':address_dict, 'aadhar_holder_name': aadhar_holder_name}

def get_lat_long_distance(loc_1,loc_2):
    distance = geodesic(loc_1, loc_2).km
    return distance

def get_lat_long(address):
    geolocator = Nominatim(user_agent='http')
    location = geolocator.geocode(address)
    return location

def get_address_string(address):
    address_list_new = ['house','loc','street','lm','vtc','dist','pc','state','country']
    address_string = ''
    for field in address_list_new:
        if field in address:
            address_string += ', ' + address[field]
    address_string = address_string[2:] 
    return address_string    

def validate_address(tenant_address,landlord_address,tenant_device_gps_address,string_threshold_level=6,km_threshold_level=1):
    lock_fields = ['country','dist','state','lm','vtc','pc']
    unlock_fields = ['street','loc','house','co']
    address_list_new = ['house','loc','street','lm','vtc','dist','pc','state','country']
    
    for field in lock_fields:
        if field in tenant_address:
            if tenant_address[field]!=landlord_address[field]:
                print("String se aya")
                return False
                
    tenant_address_string = get_address_string(tenant_address)
    landlord_address_string = get_address_string(landlord_address)
    
    tenant_lat_long = get_lat_long(tenant_address_string)
    if tenant_lat_long == None:
        print("None se aya")
        return True

    lat_long_distance = get_lat_long_distance((tenant_lat_long.latitude,tenant_lat_long.longitude),tenant_device_gps_address)
    if lat_long_distance > km_threshold_level:
        print("Distance se aya")
        return False 

    return True