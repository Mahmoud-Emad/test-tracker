"""Everything related to authentication."""
from ast import Dict
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from server.test_tracker.api.response import CustomResponse

from server.test_tracker.serializers.auth import MyTokenObtainPairSerializer, MyTokenRefreshSerializer, RegisterSerializer, UserSerializer
from server.test_tracker.services.dashboard import get_signature
from server.test_tracker.services.users import get_user_or_people



class RegisterAPIView(GenericAPIView):
    """Class RegisterAPIView to register a new user into database"""
    serializer_class = RegisterSerializer
    def post(self, request: Request) -> Response:
        """Method to register a new user"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse.success(
                data = serializer.data,
                message = "User created successfully",
                status_code=201
            )
        return CustomResponse.bad_request(
            error = serializer.errors,
            message = "User creation failed"
        )

class LoginByTokenAPIView(TokenObtainPairView):
    """Class LoginByTokenAPIView to login a user by jwt token"""
    serializer_class = MyTokenObtainPairSerializer

class MyTokenRefreshView(TokenRefreshView):
    """
    An end point to refresh the user token
    """
    serializer_class = MyTokenRefreshSerializer

class DecodeAndVerifySignatureAPIView(APIView):
    """Decode signature of a person invited"""

    def get(self, request: Request) -> Response:
        """Method to decode signature of a person invited"""
        try:
            signature = get_signature(request.query_params.get('signature'))
            data = {
                'email': signature.email,
                'first_name': signature.first_name,
                'last_name': signature.last_name,
            }
            print(signature)
            return CustomResponse.success(
                data = data
            )
        except:
            return CustomResponse.not_found(
                message = 'Signature could not be decoded, Make sure that you have a valid signature'
            )

    def put(self, request: Request) -> Response:
        """Update person obj"""
        person_signature = get_signature(request.query_params.get('signature'))
        if person_signature is not None:
            person_signature.accepted = True
            person_signature.signature = None # Remove signature from db
            person_signature.save()
            return CustomResponse.success(
                message = 'Person updated successfully',
            )
        return CustomResponse.not_found(
            message = 'Signature could not be decoded, Make sure that you have a valid signature'
        )


class GetUserAPIView(GenericAPIView):
    serializer_class = UserSerializer

    def get(self, request: Request, email: str) -> Response:
        user = get_user_or_people(email)
        if user is not None:
            return CustomResponse.success(
                data = self.get_serializer(user).data,
                message = "User found",
                status_code = 200
            )
        return CustomResponse.not_found(
            message = "User not found",
        )