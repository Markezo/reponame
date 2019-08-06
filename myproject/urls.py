"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path, re_path
from students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Students urls
    path('', views.students_list, name='home'),
    path('students/add', views.students_add, name='students_add'),
    re_path(r'^students/(?P<sid>\d+)/edit', views.students_edit, name='students_edit'),
    re_path(r'^students/(?P<sid>\d+)/delete', views.students_delete, name='students_delete'),
    # Groups urls
    path('groups', views.group_list, name='groups'),
    path('groups/add', views.groups_add, name='groups_add'),
    re_path(r'^groups/(?P<gid>\d+)/edit', views.groups_edit, name='groups_edit'),
    re_path(r'^groups/(?P<gid>\d+)/delete', views.groups_delete, name='groups_delete'),

]
