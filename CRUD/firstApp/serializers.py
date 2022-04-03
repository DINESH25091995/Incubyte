from rest_framework import serializers
from firstApp.models import Content

class ContentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Content
        fields=['id','word']
