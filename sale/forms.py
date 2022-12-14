from django import forms

CHART_CHOICE = (
    ('#1', 'Bar Graph'),
    ('#2', 'Pie Chart'),
    ('#3', 'Line Graph')
)

RESULTS_CHOICES = (
    ('#1', 'Transaction'),
    ('#2', 'Sales Date'),
    ('#3', 'Customer ID'),
    ('#4', 'Total Price')
)

class SalesSearchForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    chart_type = forms.ChoiceField(choices=CHART_CHOICE)
    results_by = forms.ChoiceField(choices=RESULTS_CHOICES)
