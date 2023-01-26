from django.contrib.auth import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class CreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
    
    def __init__(self, *args, **kwargs) -> None:
        super(CreationForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label


class AuthForm(forms.AuthenticationForm):
    def __init__(self, *args, **kwargs) -> None:
        super(AuthForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label


class PwdChangeForm(forms.PasswordChangeForm):
    def __init__(self, *args, **kwargs) -> None:
        super(PwdChangeForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label


class PwdResetForm(forms.PasswordResetForm):
    def __init__(self, *args, **kwargs) -> None:
        super(PwdResetForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label


class PwdResetConfirmForm(forms.PasswordResetForm):
    def __init__(self, *args, **kwargs) -> None:
        super(PwdResetConfirmForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label
