from django.urls import path

from todo_app import views

urlpatterns = [
    # path('',views.test1,name='new1'),
    path('',views.test2,name='new2'),
    path('page2',views.test3,name='new3'),
    path('page3',views.create,name='page3'),
    path('page4',views.read,name='page4'),
    path('delt/<int:id>/',views.delt,name='delt'),
    path('update/<int:id>/',views.update,name='update')
]