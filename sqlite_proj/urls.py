from django.urls import path
from . import views

urlpatterns = [
    path('', views.data, name='data'),
    path('adata', views.adata, name='sqlite_adata'), # here 'adata' mean add data
    path('udata/<int:id>', views.udata, name='sqlite_udata'), # here 'udata' mean update data
    path('ddata/<int:id>', views.ddata, name='sqlite_ddata'), # here 'ddata' mean delete data
     # here 'ddata' mean delete data
]