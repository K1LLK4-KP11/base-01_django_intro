from django.shortcuts import render, redirect, get_object_or_404
from .models import task

# Create your views here.


def GetTask(request):
    tasks = task.objects.all()
    return render(request, 'todo/tasks.html', {'tasks':tasks})


def add_item(request):
    if request.method == 'POST':
        title = request.POST['title']
        task.objects.create(title=title)
        return redirect('TODO')
    else:
        return render(request, 'todo/add_item.html')
    
def toggle_complete(request, item_id):
    item = get_object_or_404(task, id=item_id)
    item.complete = not item.complete
    item.save()
    return redirect('todo_list')