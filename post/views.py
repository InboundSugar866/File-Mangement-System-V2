from rest_framework import generics, authentication, permissions
from .models import File, FileDetail as FileDetailModel, Tag, FileTag
from .serializers import FileSerializer, FileDetailSerializer, TagSerializer, FileTagSerializer

class IsFileOwnedBy(permissions.BasePermission):
    message = {'detail': 'You must be the owner of this file.'}

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user

class IsTagOwnedBy(permissions.BasePermission):
    message = {'detail': 'You must be the owner of this tag.'}

    def has_object_permission(self, request, view, obj):
        # Ensure this condition correctly checks ownership
        return request.user == obj.user if hasattr(obj, 'user') else True


class IsAuthor(permissions.BasePermission):
    message = {'detail': 'You must be an author to do this.'}

    def has_permission(self, request, view):
        group_name = "Standard"
        return request.user.groups.filter(name=group_name).exists()

class FileList(generics.ListCreateAPIView):
    serializer_class = FileSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.file_set.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    lookup_field = 'filename'
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsFileOwnedBy]

class FileDetailList(generics.ListCreateAPIView):
    serializer_class = FileDetailSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsFileOwnedBy]

    def get_queryset(self):
        file = self.kwargs['file']
        return FileDetailModel.objects.filter(file__filename=file)

    def perform_create(self, serializer):
        file = File.objects.get(filename=self.kwargs['file'])
        serializer.save(file=file)

class TagList(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsAuthor]

    def get_queryset(self):
        return Tag.objects.all()

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'tagname'
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsTagOwnedBy]

class FileTagList(generics.ListCreateAPIView):
    serializer_class = FileTagSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsAuthor]

    def get_queryset(self):
        return FileTag.objects.all()

from rest_framework import generics
from .models import File, Tag, FileTag
from .serializers import FileTagSerializer

class FileTagDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FileTagSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsAuthor]

    def get_object(self):
        file_name = self.kwargs['file_name']
        tag_name = self.kwargs['tag_name']
        
        try:
            file = File.objects.get(filename=file_name)
        except File.DoesNotExist:
            raise serializers.ValidationError({"file": "File not found."})
        
        try:
            tag = Tag.objects.get(tagname=tag_name)
        except Tag.DoesNotExist:
            raise serializers.ValidationError({"tag": "Tag not found."})
        
        try:
            filetag = FileTag.objects.get(file=file, tag=tag)
        except FileTag.DoesNotExist:
            raise serializers.ValidationError({"filetag": "FileTag not found."})

        return filetag


