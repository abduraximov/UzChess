from django.db import models

class BaseModel(models.Model):
    created_at = models.Model(auto_now_add=True)
    updated_at = models.Model(auto_now=True)

    class Meta:
        abstact = True