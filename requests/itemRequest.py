import json
from flask import Response


def getItems(method):
    if(method == 'GET'):
        items = [{"name":"box","price":20},{"name":"box3","price":203}]
        return Response(json.dumps(items),  mimetype='application/json')

    elif(method == 'POST'):
        items = {"success":True}
        return Response(json.dumps(items),  mimetype='application/json')
    
# new comment