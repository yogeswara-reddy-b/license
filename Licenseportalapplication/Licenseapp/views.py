from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Client, License
from .serializers import ClientSerializer, LicenseSerializer
from django.core.mail import send_mail
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class ClientsAndThereAssociatedLicense(APIView):

    def get(self, request):

        clients = Client.objects.all()
        license_serializer = ClientSerializer(clients, many=True)
        return Response({
            'data': license_serializer.data
        })


class CreateLicence(APIView):

    def post(self, request):
        import pdb;pdb.set_trace();
        licence_serializer = LicenseSerializer(data=request.data)
        if licence_serializer.is_valid():
            licence_serializer.save()
            return Response({
                'data': licence_serializer.data
            })
        return Response({
            'error': status.HTTP_400_BAD_REQUEST,
            'message': 'Something went wrong'
        })


class SendEmailApiView(APIView):

   def post(self, request):
        msg = MIMEMultipart()
        clients = Client.objects.all()
        for client in clients:
            for licence in client.license_set.all():
                if licence.expiration_time.date() == date.today() + relativedelta(months=+4) or \
                        licence.expiration_time.date() == (
                        (date.today() + relativedelta(months=+1)) and (date.today().weekday() == 1)) or \
                        date.today() + timedelta(weeks=1):
                    message = {
                        'license_id': licence.id,
                        'license_type': licence.license_type,
                        'name_of_the_package': licence.package,
                        'expiration_date': licence.expiration_time,
                        'poc_information_of_client': {'user_name': client.user_name, 'email': client.email}
                    }
                    msg['Subject'] = 'Liciences going to expire'
                    msg.attach(MIMEText(str(message), 'plain'))
                    s = smtplib.SMTP('smtp.gmail.com', 587)
                    s.starttls()
                    s.login("yogi.b.reddy@gmail.com", "10w51a0203")
                    s.sendmail("yogi.b.reddy@gmail.com", client.admin_point_of_contact, msg.as_string())
                    s.quit()
        return Response({
            'status': status.HTTP_200_OK
        })
