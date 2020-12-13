from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cerberus import Validator
from ...models.Marca import Marca


class MarcaAPI(APIView):
    def get(self, request):
        marca = Marca.objects.filter().values()
        return Response({
            "Count": len(marca),
            "Data": marca
        }, status=status.HTTP_200_OK)

    def post(self, request):
        validator = Validator(
            {
                "name": {"required": True, "type": "string", "empty": False},
                "logo": {"required": True, "type": "string", "empty": False},
            }
        )
        if not validator.validate(request.data):
            return Response(
                {
                    "code": "invalid_body",
                    "detailed": "Cuerpo de la petición con estructura inválida",
                    "data": validator.errors,
                }, status=status.HTTP_400_BAD_REQUEST)
        marca = Marca.objects.filter(name=request.data["name"])
        if marca:
            return Response({
                "Code": "Brand_already_exist",
                "Detailled": "Brand already exist in the data base",
                "Error": "Marca existe en la base de datos"
            }, status=status.HTTP_404_NOT_FOUND)

        marca_pk = Marca.objects.create(**request.data).pk

        return Response({
            "Code": "Inserted",
            "pk": marca_pk
        }, status=status.HTTP_201_CREATED)
