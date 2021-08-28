from rest_framework import serializers
from django.db.models import fields
from invitations.models import customer

class cusSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ("name", "add", "email", "phone","password","cnfrmpass")