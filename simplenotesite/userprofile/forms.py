from userprofile.models import ProfilePicture,GMapLocation,ProfileDetails
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field
#mediapathsettings.MEDIA_ROOT
class ProfilePictureForm(ModelForm):
    class Meta:
        model = ProfilePicture
        exclude = ["user"]

class GMapLocationForm(ModelForm):    
    def __init__(self, *args, **kwargs):
        super(GMapLocationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper['address'].wrap(Field, template="userprofile/glocation.html")
    class Meta:
        model=GMapLocation


class ProfileForm(ModelForm):    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model=ProfileDetails
        exclude=['user','location']