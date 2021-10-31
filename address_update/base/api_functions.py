import requests
import uuid
import json
from bs4 import BeautifulSoup
import re

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
    # print("-"*40)
    # print(list(b_unique.children))
    # print("-"*40)
    # # address = b_unique.child

    # # if list(b_unique.children) == 0:
    # #     address = b_unique.child
    # # else:
    # #     address = str(list(b_unique.children)[0])
    # # print(address)
    print(b_unique.attrs)
    return b_unique.attrs

    # address = re.sub('\n',"",address)
    # elements = address.split('\\" ')
    # address_dict = {}
    # for element in elements:
    #     ele = element
    #     ele = re.sub('\\\\"',"",ele)
    #     ele = re.sub('\n',"",ele)
    #     ele = re.sub('/>',"",ele)
    #     ele = re.split('=|:',ele)
    #     print(ele)
    #     address_dict[ele[0]] = ele[1]
    
    # return address_dict

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
    # if res['status'].lower() =s= 'n':
    #     return {'status':res['status'], 'error_code':res['errCode']}
    
    xml_string = res['eKycString']
    address_dict = parse_xml(xml_string)
    return {'status':res['status'],'error_code':res['errCode'], 'address_dict':address_dict}
