from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from myapi.views import test_view
from myapi.views import TW2330
from myapi.views import TW2454
from myapi.views import TW2303
from myapi.views import TW2881

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'test/',test_view,name='test'),
    path(r'TW2330/', TW2330, name='TW2330'),
    path(r'TW2454/', TW2454, name='TW2454'),
    path(r'TW2303/', TW2303, name='TW2303'),
    path(r'TW2881/', TW2881, name='TW2881'),

]
# urlpatterns +=[
#     path('myapi/',include('myapi.urls')),
# ]