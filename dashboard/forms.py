from django import forms
# from api.models import User


class EmployeTypeChoiceForm(forms.Form):
    # user = forms.ModelChoiceField(queryset=User.objects.all(), required=False)

    choice = {("-", "Not Selected"), ("Internal", "Internal"), ("External", "External")}
    employee_type = forms.ChoiceField(choices=choice, required=False)

    # class Meta:
    #     model = User
    #     fields = ["user"]

    # def __init__(self, *args, **kwargs):
    #     super(EmployeTypeChoiceForm, self).__init__(*args, **kwargs)
    #     self.fields["user"].initial = self.Meta.model.objects.first()
