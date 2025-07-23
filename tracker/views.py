from django.shortcuts import render, redirect
from .models import Income, Expense
from .forms import IncomeForm, ExpenseForm
from collections import defaultdict
import json

def dashboard(request):
    income_form = IncomeForm()
    expense_form = ExpenseForm()

    if request.method == 'POST':
        if 'amount' in request.POST and 'source' in request.POST:
            income_form = IncomeForm(request.POST)
            if income_form.is_valid():
                income_form.save()
                return redirect('dashboard')
        elif 'category' in request.POST and 'amount' in request.POST:
            expense_form = ExpenseForm(request.POST)
            if expense_form.is_valid():
                expense_form.save()
                return redirect('dashboard')

    incomes = Income.objects.all()
    expenses = Expense.objects.all()

    total_income = sum(float(income.amount) for income in incomes)
    total_expense = sum(float(exp.amount) for exp in expenses)

    # Bar chart data
    category_totals = defaultdict(float)
    income_sources = defaultdict(float)

    for exp in expenses:
        category_totals[exp.category] += float(exp.amount)
    for inc in incomes:
        income_sources[inc.source] += float(inc.amount)

    labels = list(set(list(category_totals.keys()) + list(income_sources.keys())))
    expense_data = [float(category_totals.get(label, 0)) for label in labels]
    income_data = [float(income_sources.get(label, 0)) for label in labels]

    context = {
        'income_form': income_form,
        'expense_form': expense_form,
        'total_income': total_income,
        'total_expense': total_expense,
        'chart_labels': json.dumps(labels),
        'income_data': json.dumps(income_data),
        'expense_data': json.dumps(expense_data),
    }

    return render(request, 'tracker/dashboard.html', context)

def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('dashboard')

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('dashboard')

def reset_data(request):
    if request.method == 'POST':
        Income.objects.all().delete()
        Expense.objects.all().delete()
    return redirect('dashboard')
