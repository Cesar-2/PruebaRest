from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cerberus import Validator
from ...models.User import User


class UserAPI(APIView):
    def get(self, request):
        user = User.objects.filter().values()
        return Response({
            "Count": len(user),
            "Data": user
        }, status=status.HTTP_200_OK)

    def post(self, request):
        validator = Validator(
            {
                "name": {"required": False, "type": "string", "empty": False},
                "last_name": {"required": False, "type": "string", "empty": False},
                "document": {"required": False, "type": "string", "empty": False},
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

        if user:
            return Response(
                {
                    "code": "user_already_exist",
                    "detailed": "El usuraio existe en la base de datos",
                    "data": "The user already exist in data base",
                }, status=status.HTTP_409_CONFLICT)

        user_pk = User.objects.create(**request.data).pk

        return Response({
            "code": "inserted",
            "pk": user_pk
        }, status=status.HTTP_201_CREATED)
