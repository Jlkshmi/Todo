from django.urls import path

from todo_app import views

urlpatterns = [
    path('',views.test1,name='new1'),
    path('page1',views.test2,name='new2'),
    path('page2',views.test3,name='new3'),
    path('page3',views.create,name='new4')
]