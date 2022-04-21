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