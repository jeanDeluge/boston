from django import forms
from django.shortcuts import render
from .model import Model

# 변수 선택 옵션을 동적으로 생성
VARIABLE_CHOICES = [
    ('CRIM', 'CRIM'), ('ZN', 'ZN'), ('INDUS', 'INDUS'), ('NOX', 'NOX'),
    ('RM', 'RM'), ('AGE', 'AGE'), ('DIS', 'DIS'), ('RAD', 'RAD'),
    ('TAX', 'TAX'), ('PTRATIO', 'PTRATIO'), ('B', 'B'), ('LSTAT', 'LSTAT'),
]

def index(request):
    m = Model(request)
    m.get_statics()
    return render(request, 'index.html')
