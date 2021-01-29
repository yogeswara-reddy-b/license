from rest_framework import serializers

from .models import Client, License


class ClientSerializer(serializers.ModelSerializer):
    licences = serializers.CharField(source='get_licenses', read_only=True)

    class Meta:
        model = Client
        fields = '__all__'


class ClientsEmailSerializer(serializers.ModelSerializer):
    send_email = serializers.CharField(source='send_emails', read_only=True)

    class Meta:
        model = Client
        fields = '__all__'


class LicenseSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = License
        fields = '__all__'




