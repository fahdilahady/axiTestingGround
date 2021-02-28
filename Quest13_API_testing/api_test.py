
from apiLibrary.api_lib import api_lib
import json
global curProdId

curProdId = 100

def storeProductId(_id):
    global curProdId
    curProdId = _id
    pass

def test_ableToCreateNewProduct(prodName="Cara cepat dapat jodoh", description="buku", image="someimage.png", price=0, status=False):
    api = api_lib()
    resp = api.createProduct(prodName, description, image, price=1000, status=True)
    assert resp is not None
    assert resp.status_code == 200
    assert resp.text !=""
    body = json.loads(resp.text)
    assert body["code"] == 201
    createdProductId = body["data"]["id"]
    assert createdProductId > 0
    storeProductId(createdProductId)
    
def test_ableToSeeDetailProductRecentlyCreated():
    print("last created product id: "+str(curProdId))
    assert curProdId>0
    api = api_lib()
    resp = api.getProduct(curProdId)
    assert resp is not None
    assert resp.status_code == 200
    assert resp.text !=""
    body = json.loads(resp.text)
    assert body["code"] == 200
    assert body["data"]["id"] == curProdId

def test_ableToUpdateProduct():
    api=api_lib()
    resp = api.updateProduct(curProdId, prodName="Kerang Ajaib", description="SpngBob", discount_amount=100, status=True)
    assert resp is not None
    assert resp.status_code == 200
    assert resp.text !=""
    body = json.loads(resp.text)
    assert body["code"] == 200

def test_ableToDeleteProduct():
    api = api_lib()
    resp = api.deleteProduct(curProdId)
    assert resp is not None
    assert resp.status_code == 200
    assert resp.text !=""
    body = json.loads(resp.text)
    assert body["code"] == 204