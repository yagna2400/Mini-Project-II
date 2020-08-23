from django.urls import path
from . import views
urlpatterns=[
  path('',views.home,name='home'),
  #path('',view.login,name='login'),
  #path('',views.schemaview,name='schemaview'),
]