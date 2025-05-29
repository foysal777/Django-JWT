
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from .utils import generate_otp, send_otp_email
from rest_framework import status

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if CustomUser.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=400)
        if CustomUser.objects.filter(email=email).exists():
            return Response({'error': 'Email already registered'}, status=400)

        otp = generate_otp()
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_active=False,
            otp=otp
        )
        send_otp_email(user.email, otp)
        return Response({'message': 'User created. OTP sent to your email.'}, status=201)