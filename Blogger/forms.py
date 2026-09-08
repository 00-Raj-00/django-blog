from django import forms


from .models import User,Article

class Register_form(forms.ModelForm):
    confirm_password= forms.CharField(widget=forms.PasswordInput)
    class Meta :
        model=User
        fields = ['first_name','username','email','password',]

        widgets = {
               'password' : forms.PasswordInput,
               'username'  : forms.TextInput(attrs={
                   'placeholder':'create author name'
               })
         }

    def clean(self):
        clean_data= super().clean()
        password = clean_data.get('password')
        confirm_password=clean_data.get('confirm_password')
        if confirm_password != password:
            raise forms.ValidationError('Password not matched')




        username = clean_data.get('username')
        if User.objects.filter(username= username):
             raise  forms.ValidationError('Author Name Taken')
        return clean_data




class Arti_form(forms.ModelForm):
    class Meta :
     model = Article
     fields = ['image','title','intro','body','conc',]



class login_form(forms.Form):
   author =forms.CharField()
   password= forms.CharField(widget=forms.PasswordInput)