from django.db import models

class Node(models.Model):
    id = models.CharField(max_length=60, primary_key=True)
    status = models.CharField(max_length=60)

    def __str__(self):
        return f"id:{self.id}, status:{self.status}"