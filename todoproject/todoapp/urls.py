from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('details',views.detail,name='detail'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.TaskDetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteview.as_view(),name='cbvdelete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


