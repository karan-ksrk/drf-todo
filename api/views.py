from rest_framework.response import Response
from .models import Todo, User
from rest_framework.authentication import TokenAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def api_overview(request):
    api_urls = {
        'user': request.user.username,
        'List': '/list/',
        'Detail View': '/api/<int:pk>/',
        'Create': '/api/create/',
        'Update': '/api/update/<int:pk>/',
        'Delete': '/api/delete/<int:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_todos(request):
    todo_status = request.GET.get('status')
    if todo_status:
        if todo_status == 'completed':
            todos = Todo.objects.filter(completed=True, )
        elif todo_status == 'uncompleted':
            todos = Todo.objects.filter(completed=False)
        else:
            todos = Todo.objects.all()
    else:
        todos = Todo.objects.filter(user=request.user)
    todos_json = [todo.to_json() for todo in todos]
    return Response(todos_json)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_todo_detail(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
    except Todo.DoesNotExist:
        return Response({'error': 'Todo not found'})
    return Response(todo.to_json())

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_todo(request):
    title = request.POST['title']
    completed = request.POST.get('completed')
    if completed:
        completed = True if completed == 'true' else False
    else:
        completed = False
    user = request.user
    todo = Todo.objects.create(user=user, title=title, completed=completed)
    return Response(todo.to_json())

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_todo(request):
    todo = Todo.objects.get(id=request.POST['id'])
    title = request.POST.get('title')
    completed = request.POST.get('completed')

    if title:
        todo.title = title
    if completed:
        todo.completed = True if completed == 'true' else False
    todo.save()
    return Response(todo.to_json())

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_todo(request):
    Todo.objects.get(id=request.POST['id']).delete()
    return Response({'message': 'Todo deleted'})