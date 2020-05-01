#***** for NXOSv *****
import requests
import json

#****** start of ASAv modification *****

url = "https://192.168.10.100/api/objects/networkobjects"

payload = "{\r\n  \"host\": {\r\n    \"kind\": \"IPv4Address\",\r\n    \"value\": \"100.1.1.1\"\r\n  },\r\n  \"kind\": \"object#NetworkObj\",\r\n  \"name\": \"Development\",\r\n  \"objectId\": \"Development\"\r\n}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic ZW5hYmxlXzE6Y2lzY28="
    }

response = requests.request("POST", url, data=payload, verify=False, headers=headers)

print(response.text)

#***** end of adding Development  with an IP address of 100.1.1.1 on ASAv *****
#***** start of NXOSv modification ***

url='http://192.168.10.60/ins'
switchuser='admin'
switchpassword='Passw0rd1'

myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "conf t ;vlan 600 ;name Construction ; vlan 700 ;name Analysis ;",
    "output_format": "json"
  }
}
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

#***** end of NXOSv *****
#***** start of add static route to 10.1.1.1 *****
#***** already done ***** import requests

url = "http://192.168.10.80/restconf/api/config/native/ip/route"

querystring = {"deep":""}

payload = "<route xmlns=\"http://cisco.com/ns/yang/ned/ios\" xmlns:y=\"http://tail-f.com/ns/rest\"  xmlns:ios=\"http://cisco.com/ns/yang/ned/ios\">\n    <ip-route-interface-forwarding-list>\n        <prefix>216.48.1.0</prefix>\n        <mask>255.255.255.0</mask>\n        <fwd-list>\n            <fwd>10.1.1.1</fwd>\n        </fwd-list>\n    </ip-route-interface-forwarding-list>\n    <static>\n  </static>\n</route>"
headers = {'Authorization': 'Basic YWRtaW46Y2lzY28='}

response = requests.request("PUT", url, data=payload, headers=headers, params=querystring)

print(response.text)

