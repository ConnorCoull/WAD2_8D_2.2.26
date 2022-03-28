from django import forms 
from django.contrib.auth.models import User
from jot.models import UserProfile,Book,Review

#might not need this, check how registration is interacting with models 
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    
class UserProfileForm(forms.ModelForm):
    user_picture = forms.ImageField()
    
    class Meta:
        model = UserProfile
        exclude = ('user','bio','user_picture_file')

#Do i need to add the book being reviewed and the user reviewing it as a hidden field?
class ReviewForm(forms.ModelForm):
    review_content  = forms.CharField(max_length=250)
    #Maybe radio buttons insted 
    review_rating = forms.IntegerField(min_value=1,max_value=5)
    class Meta:
        model = Review
        fields = ('review_rating','review_content')
    
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_title',
                  'author',
                  'book_description',
                  'pdf_upload',
                  'book_category',
        )
