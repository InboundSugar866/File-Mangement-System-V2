from django.urls import path
from . import views

app_name = 'file_management'

urlpatterns = [
    path('files/', views.FileList.as_view(), name='file_list'),
    path('files/<str:filename>/', views.FileDetailView.as_view(), name='file_detail'),
    path('files/<str:file>/details/', views.FileDetailList.as_view(), name='file_detail_list'),
    path('tags/', views.TagList.as_view(), name='tag_list'),
    path('tags/<str:tagname>/', views.TagDetail.as_view(), name='tag_detail'),
    path('filetags/', views.FileTagList.as_view(), name='filetag_list'),
    path('filetags/<str:file_name>/<str:tag_name>/', views.FileTagDetail.as_view(), name='filetag_detail_by_name'),
]
