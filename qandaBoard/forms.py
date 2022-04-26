from django import forms

class DeleteBoardForm(forms.Form):
    delete_YN = forms.CharField(max_length=1, required=False)
    id = forms.IntegerField(max_value=None)
    board_id = forms.IntegerField(max_value = None)

class ReplyForm(forms.Form):
    board_id = forms.IntegerField(max_value=None)
    user_id = forms.IntegerField(max_value=None)
    reply_content = forms.CharField(max_length=1500, required=True)
