from django.shortcuts import render
from django.http import HttpResponse, response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django.core.mail import send_mail

from django.conf import settings

from .serializers import ContactFormSerializer
from .models import ContactForm

class ContactFormAPI(APIView):

    def post(self, request):
        serializer = ContactFormSerializer(data=request.data)

        if serializer.is_valid():
            first_name = serializer.validated_data.get(
                'first_name')
            last_name = serializer.validated_data.get(
                'last_name')
            email = serializer.validated_data.get(
                'email')
            phone = serializer.validated_data.get(
                'phone')
            country = serializer.validated_data.get(
                'country')
            details = serializer.validated_data.get(
                'details')

            try:
                send_mail(
                    from_email=email,
                    subject=first_name + ' ' + last_name +
                    ' ' + str(datetime.now()),
                    message=details,
                    recipient_list=[settings.EMAIL_ADMIN],
                    fail_silently=False,
                )
            except Exception as e:
                print(e)
                return Response({"Error": {"code": 500, "message": "email send error"}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
