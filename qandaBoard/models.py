from django.db import models
from django.db.models.fields import *
from bbuser.models import User

# Create your models here.
class Board(models.Model):
    board_id = AutoField(primary_key=True, db_column='board_id')
    board_title = CharField(max_length=50, null = False, db_column='board_title')
    board_content = TextField(max_length = None, null = False, db_column='board_content' )
    board_reg_date = DateTimeField(auto_now_add=True, null = False, db_column='board_reg_date')
    board_mod_date = DateTimeField(auto_now=True, null = True, db_column='board_mod_date')
    board_deleted = CharField(max_length=1, default = 'N', db_column='board_deleted')
    
    #외래키
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, db_column='user_id')
    
    class Meta:
        db_table = 'board'

#댓글
class Reply(models.Model):
    reply_id=models.AutoField(primary_key=True,db_column='reply_id')
    reply_content=models.CharField(max_length=200,db_column='reply_content',null=False)
    reg_date=DateTimeField(auto_now=True,db_column='reg_date',null=False)
    reply_deleted=CharField(max_length=1, null=False, db_column='reply_deleted')

    #외래키
    user=models.ForeignKey(User, on_delete=models.CASCADE, null = False, db_column='user_id', related_name='reply_user_relations')
    board=models.ForeignKey(Board, on_delete=models.CASCADE,null=False, db_column='board_id', related_name='reply_board_relations')

    class Meta:
        db_table = 'reply'