from django.db import models

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
    def __str__(self):
        return self.question_text



class ListInput(models.Model):
    # title = models.ForeignKey(Type, on_delete=models.CASCADE, db_column="title")
    question_text = models.ForeignKey(CheckList, on_delete=models.CASCADE, db_column="question_text")
    # question_date = models.DateField(auto_now_add=True)
    answer = models.BooleanField(null=True)
    bigo = models.CharField(blank=True, default="", max_length=100)
    
    # def __str__(self):
    #     return str(self.question_date)



# class History(models.Model):
#     title = models.ForeignKey(Type, on_delete=models.CASCADE, db_column="title")
#     question_date = models.ForeignKey(ListInput, on_delete=models.CASCADE, db_column="date")




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