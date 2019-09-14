from django import forms
from crudapplication.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # if no need to all field
        # fields = ("eid", "ename")
        fields = "__all__"
