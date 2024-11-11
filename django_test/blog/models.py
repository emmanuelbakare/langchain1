from django.db import models

class BlogPost(models.Model):
    """
    Represents a blog post in the application.

    This model stores information about individual blog posts, including
    their title, description, tags, and timestamps for creation and updates.
    """

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, help_text="The title of the blog post")
    description = models.TextField(help_text="The main content of the blog post")
    tags = models.CharField(max_length=255, help_text="Comma-separated tags for the blog post")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the post was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the post was last updated")

    def __str__(self):
        """
        Returns a string representation of the BlogPost.

        :return: The title of the blog post
        :rtype: str
        """
        return self.title

    class Meta:
        ordering = ['-created_at']  # Order blog posts by creation date, newest first
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"