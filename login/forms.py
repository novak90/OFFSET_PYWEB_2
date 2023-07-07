from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField
from django.forms import EmailField

def validate_user(value):
    if not User.objects.filter(username=value).exists():
        raise ValidationError('User Does Not Exist')
    return value


user = UsernameField(validators=[validate_user])


def validate_email(value):
   if User.objects.filter(email=value).exists():
       raise ValidationError('Email Already Exists')
   return value


email = EmailField(validators=[validate_email])
class CustomUserCreationForm(UserCreationForm):
    email = EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email Already Exists')

        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        field_classes = {"username": UsernameField}
