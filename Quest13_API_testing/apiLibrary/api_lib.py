import sys
sys.path.append('../')
import requests
import json  

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

class api_lib:
  def __init__(self, tokenSession = "e3479c4068b18c10ce220f5665f1c206bff27b3e9a722bcc35cf52e36708a1fb"):
    self.url = "https://gorest.co.in/public-api/products"
    self.sessionToken = BearerAuth(tokenSession)
    pass
  
  def getProduct(self, id=""):
    payload={}
    headers = {}
    _url = self.url + "/"+str(id) if id != "" else self.url
    response = requests.request("GET", _url, headers=headers, data=payload, auth=self.sessionToken)
    return response
  
  def createProduct(self, prodName, description, image="", price = 0, status=False):
    payload = {"name":prodName, "description":description,"image":image,"price":price,"status":status}
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps(payload, indent = 4)
    response = requests.request("POST", self.url, headers=headers, data=payload, auth=self.sessionToken)
    return response
    

  def updateProduct(self, id, prodName="",description="", discount_amount="", status=""):
    payload = {}
    if prodName != "":
      payload["name"] = prodName
    if description != "":
      payload["description"] = description
    if discount_amount != "":
      payload["discount_amount"] = discount_amount
    if discount_amount != "":
      payload["status"] = status
    payload = json.dumps(payload, indent = 4)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("PUT", self.url+"/"+str(id), headers=headers, data=payload, auth=self.sessionToken)
    return response

  def deleteProduct(self, id):
    payload = {}
    headers = {}
    response = requests.request("DELETE", self.url+"/"+str(id), headers=headers, data=payload, auth=self.sessionToken)
    return response