"""
Model demonstrating protected files.
"""
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import models


class SecretDocumentStorage(FileSystemStorage):
    "Storage for secrets"

    def url(self, name):
        """
        Send document urls through icanhaz
        """
        return '/icanhaz' + super(SecretDocumentStorage, self).url(name)


class SecretDocument(models.Model):
    """
    Important documents, don't let anyone download them
    """
    name = models.CharField(max_length=200)
    owned_by = models.ForeignKey(User)
    documents = models.FileField(upload_to="protected")

    def __unicode__( self ):
        return self.name
