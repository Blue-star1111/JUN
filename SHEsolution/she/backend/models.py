from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

# Create your models here.

class Type(models.Model):
    title = models.CharField(max_length=100, unique=True, null=False)
    
    def __str__(self):
        return self.title


class CheckList(models.Model):
    title = models.ForeignKey(Type, on_delete=models.CASCADE, db_column="title")
    question_text = models.CharField(max_length=200,
                                    unique=True, 
                                    null=False,
                                    default=None,
                                    blank=False)
    answer = models.BooleanField(null=True)
    bigo = models.CharField(blank=True, default="", max_length=100)

# class History(models.Model):
#     title = models.ForeignKey(Type, on_delete=models.CASCADE, db_column="title")
#     date = models.DateTimeField()

class OverwriteStorage(FileSystemStorage):

    def get_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

class ImageDetect(models.Model):
    image = models.ImageField(upload_to="yolov5/images", storage=OverwriteStorage())



# 테이블 전체 삭제
# DO $$ DECLARE
#     r RECORD;
# BEGIN
#     -- if the schema you operate on is not "current", you will want to
#     -- replace current_schema() in query with 'schematodeletetablesfrom'
#     -- *and* update the generate 'DROP...' accordingly.
#     FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = current_schema()) LOOP
#         EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
#     END LOOP;
# END $$;

# 테이블 초기화
# delete from backend_imagedetect;
# alter SEQUENCE backend_imagedetect_id_seq restart 1;