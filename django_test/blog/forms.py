from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    """
    Form for creating and updating BlogPost instances.
    
    This form includes fields for the title, description, and tags of a blog post.
    It excludes the automatically generated fields like id, created_at, and updated_at.
    """
    
    class Meta:
        model = BlogPost
        fields = ['title', 'description', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title of your blog post'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write your blog post content here'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter tags separated by commas'}),
        }
        labels = {
            'title': 'Blog Post Title',
            'description': 'Content',
            'tags': 'Tags',
        }

    def clean_tags(self):
        """
        Custom cleaning method for the tags field.
        
        This method strips whitespace from the beginning and end of each tag,
        and ensures that tags are stored in a consistent format.
        """
        tags = self.cleaned_data.get('tags')
        if tags:
            # Split tags by comma, strip whitespace, and rejoin
            tags = ','.join([tag.strip() for tag in tags.split(',')])
        return tags