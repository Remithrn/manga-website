from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cover = models.ImageField(upload_to='covers')
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    