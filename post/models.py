from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

def upload_to(instance, filename):
    return f'files/{filename}'

class FileCommonInfo(models.Model):
    filename = models.CharField(max_length=255)
    filepath = models.FileField(upload_to=upload_to)
    uploaded_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def clean(self):
        if File.objects.filter(filename=self.filename).exists():
            raise ValidationError("A file with this name already exists.")

    def delete(self, *args, **kwargs):
        self.filepath.delete()
        super().delete(*args, **kwargs)

class File(FileCommonInfo):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.filename

    class Meta:
        db_table = 'file'

class FileDetail(models.Model):
    file = models.OneToOneField(File, on_delete=models.CASCADE, unique=True)
    filesize = models.IntegerField()
    filetype = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Details of {self.file.filename}"

    objects = models.Manager()

    class Meta:
        db_table = 'file_detail'

class Tag(models.Model):
    tagname = models.CharField(max_length=50)

    def __str__(self):
        return self.tagname

    class Meta:
        db_table = 'tag'

class FileTag(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        db_table = 'file_tag'
