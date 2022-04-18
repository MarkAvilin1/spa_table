from django import forms


class SortForm(forms.Form):
    sorting = forms.ChoiceField(label='Sorting by', required=False,
                                choices=[
                                    ['id', '------'],
                                    ["title", 'Title'],
                                    ['quantity', 'Quantity'],
                                    ['distance', 'Distance']])


class FilterForm(forms.Form):
    categories = forms.ChoiceField(label='Categories', required=False,
                                   choices=[
                                       ['', '------'],
                                       ['title', 'Title'],
                                       ['quantity', 'Quantity'],
                                       ['distance', 'Distance']])

    condition = forms.ChoiceField(label='Condition', required=False,
                                  choices=[
                                      ['', '------'],
                                      ['equal', 'Equal to'],
                                      ['contains', 'Contain'],
                                      ['gt', 'Great than'],
                                      ['lt', 'Less than']])

    choose = forms.CharField(label='Choose', required=False,
                             widget=forms.TextInput(attrs={'placeholder': 'Text or number...'}))
