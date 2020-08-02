from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Todo

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
        content = json.loads(request.body)['content']
        todo = Todo(content=content)
        todo.save()
        newTodo = Todo.objects.order_by("id").last()
        params = {
            'id': newTodo.id,
            'content': newTodo.content,
            'is_end': newTodo.is_end,
            'deleted_at': newTodo.deleted_at,
        }
        json_str = json.dumps(params, ensure_ascii=False, indent=2) 
        return HttpResponse(json_str)

# # 新しいtodo作成
# def save(request):
