import sys
import requests

# open file to read
f = open('F:\\darren\\05_programming\\09_javaScript\\igIndex\\credentials.txt','r')
x, y, z = f.readline(), f.readline(), f.readline()


# IG rest API parameters

rest_api_key = f.readline()     #"<your ig api key>"
rest_identifier = f.readline()  #"<your ig username>"
rest_password = f.readline()    #"<your ig password>"

print('IG rest API parameters imported')

# close file once read
f.close()


# IG rest login request

rest_url = "https://api.ig.com/gateway/deal/session"

headers = {}
headers["Content-Type"] = "application/json; charset=UTF-8"
headers["Accept"] = "application/json; charset=UTF-8"
headers ["Version"] = "2"
headers ["X-IG-API-KEY"] = rest_api_key

request_json = {}
request_json["identifier"] = rest_identifier
request_json["password"] = rest_password

rest_response = requests.request("POST", rest_url, headers=headers, json=request_json)
if rest_response.status_code != 200:
    print("error", rest_response.status_code, rest_url, rest_response.text)
    sys.exit(0)

# collect params from IG rest login response

xst = rest_response.headers["X-SECURITY-TOKEN"]
cst = rest_response.headers["CST"]

response_json = rest_response.json()
current_account = response_json["currentAccountId"]
lightstreamer_endpoint = response_json["lightstreamerEndpoint"]

# IG streaming login request

streaming_url = "{}/lightstreamer/create_session.txt".format(lightstreamer_endpoint)

steaming_user = current_account;
steaming_password = "CST-{}|XST-{}".format(cst, xst)

query = {}
query["LS_op2"] = "create"
query["LS_cid"] = "mgQkwtwdysogQz2BJ4Ji kOj2Bg"
query["LS_user"] = steaming_user
query["LS_password"] = steaming_password

streaming_response = requests.request("POST", streaming_url, data=query, stream=True)
if streaming_response.status_code != 200:
    print("error", streaming_response.status_code, streaming_url, streaming_response.text)
    sys.exit(0)

# collect params from streaming response

streaming_session = None
control_domain = None
streaming_iterator = streaming_response.iter_lines(chunk_size=80, decode_unicode=True)
for line in streaming_iterator:
    print("line", line)
    if ":" not in line:
        continue
    [param,value] = line.split(":",1)
    if param == "SessionId":
            streaming_session = value
    if param == "ControlAddress":
        control_domain = value
    if streaming_session and control_domain:
        break

# open control connection and subscribe EURUSD

control_url = "https://{}/lightstreamer/control.txt".format(control_domain)

query = {}
query["LS_session"] = streaming_session
query["LS_op"]="add"
query["LS_table"]="1"
query["LS_id"]="MARKET:CS.D.EURUSD.MINI.IP"
query["LS_schema"]="BID OFFER"
query["LS_mode"]="MERGE"

control_response = requests.request("POST", control_url, data=query)
if control_response.status_code != 200:
    print("error", control_response.status_code, control_url, control_response.text)
sys.exit(0)

# stream prices

for line in streaming_iterator:
    print("line", line)
