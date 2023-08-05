from django.db import models

# Create your models here.


class Info(models.Model):
    """Model definition for Info."""
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=245)
    subject = models.TextField(max_length=200)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Info."""

        verbose_name = 'Info'
        verbose_name_plural = 'Infos'

    def __str__(self):
        """Unicode representation of Info."""
        return str(self.email)

# todo pdf model 

class PDFDocument(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/')
