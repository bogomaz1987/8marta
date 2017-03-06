from django.conf.urls import url
from django.contrib import admin
from girls.views import Spisok, Login, Logout

urlpatterns = [
    url(r'^$', Login.as_view(), name='login'),
    url(r'^admin/', admin.site.urls),
    url(r'^main/', Spisok.as_view(), name='spisok'),
    url(r'^logout/', Logout.as_view(), name='logout')
]

