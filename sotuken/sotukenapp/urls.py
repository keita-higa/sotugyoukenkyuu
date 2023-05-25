from django.urls import path
from .views import loginfunc, signupfunc,  homefunc, mypagefunc, logoutfunc, detailfunc, SotukenCreate, goodfunc, readfunc

urlpatterns = [
    path('login/', loginfunc, name='login'),
    path('signup/', signupfunc, name='sign'),
    path('home/', homefunc, name='home'),
    path('mypage/', mypagefunc, name='mypage'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('create/', SotukenCreate.as_view(), name='create'),
    path('good/<int:pk>', goodfunc, name="good"),
    path('read/<int:pk>', readfunc, name="read"),
]