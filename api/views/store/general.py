from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cerberus import Validator
from ...models.Tienda import Tienda
from ...models.Marca import Marca


class TiendaAPI(APIView):
    def get(self, request):
        tienda = Tienda.objects.filter().values()
        return Response({
            "Count": len(tienda),
            "Data": tienda
        }, status=status.HTTP_200_OK)

    def post(self, request):
        validator = Validator(
            {
                "brand": {"required": True, "type": "integer", "empty": False},
                "identifier": {"required": True, "type": "string", "empty": False},
                "name": {"required": True, "type": "string", "empty": False},
                "thumbnail": {"required": True, "type": "string", "empty": False},
                "address": {"required": True, "type": "string", "empty": False}
            }
        )
        if not validator.validate(request.data):
            return Response(
                {
                    "code": "invalid_body",
                    "detailed": "Cuerpo de la petición con estructura inválida",
                    "data": validator.errors,
                }, status=status.HTTP_400_BAD_REQUEST)

        marca = Marca.objects.filter(pk=request.data["brand"]).first()

        if not marca:
            return Response({
                "Code": "Brand_doesnt_exist",
                "Detailled": "Brand doesn't exist in the data base",
                "Error": "Marca no fue encontrada"
            }, status=status.HTTP_404_NOT_FOUND)

        if Tienda.objects.filter(name=request.data["name"]):
            return Response({
                "Code": "Store_already_exist",
                "Detailled": "Store already exist in the data base",
                "Error": "La tienda ya existe en la base de datos"
            }, status=status.HTTP_409_CONFLICT)

        del request.data["brand"]
        tienda_pk = Tienda.objects.create(**request.data, brand=marca).pk

        return Response({
            "Code": "Inserted",
            "pk": tienda_pk
        }, status=status.HTTP_201_CREATED)
