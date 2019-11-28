import json

from django.http import HttpResponse
from django.core.serializers import serialize

class Employee_mixin(object):
    def response_mixin(self, d1):
        json_data = json.dumps(d1)
        return HttpResponse(json_data, content_type='application/json')

#specific one Employee Details
class Employee_serialize_mixin(object):
    def response2_mixin(self, res):
        json_data = serialize('json', [res])
        return HttpResponse(json_data, content_type='application/json')

#get all Employee Details
class Employee_serialize2_mixin(object):
    def response2_mixin(self, res):
        json_data = serialize('json', res)
        return HttpResponse(json_data, content_type='application/json')