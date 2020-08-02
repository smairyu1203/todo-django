from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Todo

@ensure_csrf_cookie
# Create your views here.
# 全返却
def index(request):
    #気持ち悪いので後でいい案探す
    if request.method == 'GET':
        todos = Todo.objects.values()
        params = [todo for todo in todos]
        json_str = json.dumps(params, ensure_ascii=False, indent=2) 
        return HttpResponse(json_str)

    elif request.method == 'POST':
        todo = Todo(content=request.content)
        todo.save()
        param = todo.values
        json_str = json.dumps(param, ensure_ascii=False, indent=2) 

        return HttpResponse(json_str)

# # 新しいtodo作成
# def save(request):