from django import forms
from .models import Income, Expense, SavingGoal

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = '__all__'

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'

class SavingGoalForm(forms.ModelForm):
    class Meta:
        model = SavingGoal
        fields = '__all__'
