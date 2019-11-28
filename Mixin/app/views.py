from django.views.generic import View

from .mixin import Employee_mixin, Employee_serialize_mixin, Employee_serialize2_mixin
from .models import Employee, Student

#send the data Dictionary
class Employee_info1(Employee_mixin, View):
    def get(self, request):
        d1 = {'idno':101, 'name':"Mithila", 'salary': 250000}
        return self.response_mixin(d1)

#send one Employee data from database
class Employee_info2(Employee_serialize_mixin, View):
    def get(self, request):
        res = Employee.objects.get(idno=101)
        return self.response2_mixin(res)


class Employee_info3(Employee_serialize_mixin, View):
    def get(self, request):
        res = Student.objects.get(rollno=1003)
        return self.response2_mixin(res)

