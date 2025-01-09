from rest_framework import serializers
from .models import File, FileDetail, Tag, FileTag

class FileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = File
        fields = ('filename', 'filepath', 'uploaded_date', 'user')

class FileDetailSerializer(serializers.HyperlinkedModelSerializer):
    file_slug = serializers.SlugRelatedField(
        read_only=True,
        source='file',
        slug_field='filename'
    )

    file = serializers.HyperlinkedRelatedField(
        view_name='file_management:file_detail',
        read_only=True,
        lookup_field='filename'
    )

    class Meta:
        model = FileDetail
        fields = ('file_slug', 'filesize', 'filetype', 'created_date', 'modified_date', 'file')
        read_only_fields = ['file',]

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('tagname',)

from rest_framework import serializers
from .models import File, Tag, FileTag

from rest_framework import serializers
from .models import File, Tag, FileTag

class FileTagSerializer(serializers.ModelSerializer):
    file = serializers.CharField()
    tag = serializers.CharField()

    class Meta:
        model = FileTag
        fields = ['file', 'tag']

    def create(self, validated_data):
        filename = validated_data['file']
        tagname = validated_data['tag']

        try:
            file = File.objects.get(filename=filename)
        except File.DoesNotExist:
            raise serializers.ValidationError({"file": "File not found."})

        try:
            tag = Tag.objects.get(tagname=tagname)
        except Tag.DoesNotExist:
            raise serializers.ValidationError({"tag": "Tag not found."})

        filetag = FileTag.objects.create(file=file, tag=tag)
        return filetag

    def update(self, instance, validated_data):
        filename = validated_data.get('file', instance.file.filename)
        tagname = validated_data.get('tag', instance.tag.tagname)

        try:
            file = File.objects.get(filename=filename)
        except File.DoesNotExist:
            raise serializers.ValidationError({"file": "File not found."})

        try:
            tag = Tag.objects.get(tagname=tagname)
        except Tag.DoesNotExist:
            raise serializers.ValidationError({"tag": "Tag not found."})

        instance.file = file
        instance.tag = tag
        instance.save()
        return instance


