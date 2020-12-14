import base64
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cerberus import Validator
from ...models.User import User
from django.core.mail import send_mail
import requests
from django.conf import settings


class AuthAPI(APIView):
    def post(self, request):
        validator = Validator(
            {
                "email": {"required": True, "type": "string", "empty": False},
                "password": {"required": True, "type": "string", "empty": False}
            }
        )
        if not validator.validate(request.data):
            return Response(
                {
                    "code": "invalid_body",
                    "detailed": "Cuerpo de la petición con estructura inválida",
                    "data": validator.errors,
                }, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=request.data["email"]).values()

        if not user:
            return Response(
                {
                    "code": "user_doesnt_exist",
                    "detailed": "El usuario no existe en la base de datos",
                    "data": "The user doesnt exist in data base",
                }, status=status.HTTP_404_NOT_FOUND)

        password = User.objects.filter(
            email=request.data["email"], password=request.data["password"]).first()
        if not password:
            return Response(
                {
                    "code": "invalid_password",
                    "detailed": "La contraseña es incorrecta",
                    "data": "Invalid password",
                }, status=status.HTTP_409_CONFLICT)
        email = password.email
        access_token(email)

        return Response({
            "code": "access token sended to the email",
            "data": "token de acceso enviado al correo",
        }, status=status.HTTP_200_OK)


def access_token(email):
    client_id = "tiaSehsvFNyH49Jyv3i5AOHacfzJnd0yqVhwSgVs"
    secret = "TIaWf2wkQe4nQPYABOy53dN3IgM5Qs1QnJTTT6gOxdiFTl22F7vdCeFfKkHgMEnjDMj6FmGDVqSoVTHwdHxYmNBlQfeDDawxilO4iYhS6tw8DKj3NMfoGEkhvpZavVQC"
    credential = "{0}:{1}".format(client_id, secret)
    base = base64.b64encode(credential.encode()).decode()
    url = "http://127.0.0.1:8000/o/token/"
    all_headers = {
        "Authorization": "Basic %s" % base,
        "Content-Type": "application/x-www-form-urlencoded",
        "Cache-Control": "no-cache"
    }
    data = {"grant_type": "client_credentials"}
    request = requests.post(url, data=data, headers=all_headers)
    data = request.json()
    access_token = str(data["access_token"])
    msj = "el token es: {}".format(access_token)
    type(msj)
    send_mail(
        "prueba authentication",
        msj,
        settings.EMAIL_HOST_USER,
        [email]
    )
