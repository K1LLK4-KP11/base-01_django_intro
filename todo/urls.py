from django.urls import path
from todo import views 
from todo.views import add_item, toggle_complete

urlpatterns = [
    path('TODO/', views.GetTask, name='TODO'),
    path('add/', add_item, name='add_item'),
    path('toggle_complete/<int:item_id>/', toggle_complete, name='toggle_complete'),
]
