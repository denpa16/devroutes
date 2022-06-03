from unicodedata import name
from django import forms
from .fields import ListTextWidget

class FormForm(forms.Form):
    start_point = forms.CharField(label='Отправление',required=True)
    end_point = forms.CharField(label='Прибытие',required=True)

    def __init__(self, *args, **kwargs):
        _start_list = kwargs.pop('start_list', None)
        _end_list = kwargs.pop('end_list', None)
        super(FormForm, self).__init__(*args, **kwargs)

    # the "name" parameter will allow you to use the same widget more than once in the same
    # form, not setting this parameter differently will cuse all inputs display the
    # same list.
        self.fields['start_point'].widget = ListTextWidget(data_list=_start_list, name='country-list')
        self.fields['end_point'].widget = ListTextWidget(data_list=_end_list, name='country-list')