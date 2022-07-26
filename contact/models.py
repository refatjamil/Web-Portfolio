from django.db import models

# Create your models here.

class Message(models.Model):
    m_Name = models.CharField(max_length=100,null=True)
    m_Email =models.CharField(max_length=100,null=True)
    m_Subject =models.CharField(max_length=100,null=True)
    m_Message =models.CharField(max_length=100,null=True)

    class Meta:
        db_table = "Message"
    
    def __str__(self):
        return self.m_Name
