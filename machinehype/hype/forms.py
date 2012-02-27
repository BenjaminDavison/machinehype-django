from django.db import models
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from models import UserProfile
 
class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        try:
            self.fields['email'].initial = self.instance.user.email
            # self.fields['first_name'].initial = self.instance.user.first_name
            # self.fields['last_name'].initial = self.instance.user.last_name
        except UserProfile.DoesNotExist:
            pass
    
    class Meta:
        model = UserProfile
        exclude = ('user',)        