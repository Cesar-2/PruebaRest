from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cerberus import Validator
from ...models.Tienda import Tienda
from ...models.Oferta import Oferta


class DealAPI(APIView):
    def get(self, request):
        deal = Oferta.objects.filter().values()
        return Response({
            "Count": len(deal),
            "Data": deal
        }, status=status.HTTP_200_OK)

    def post(self, request):
        validator = Validator(
            {
                "name": {"required": True, "type": "string", "empty": False},
                "store": {"required": True, "type": "integer", "empty": False},
                "image": {"required": True, "type": "string", "empty": False},
                "price": {"required": True, "type": "integer", "empty": False}
            }
        )
        if not validator.validate(request.data):
            return Response(
                {
                    "code": "invalid_body",
                    "detailed": "Cuerpo de la petición con estructura inválida",
                    "data": validator.errors,
                }, status=status.HTTP_400_BAD_REQUEST)

        tienda = Tienda.objects.filter(pk=request.data["store"]).first()

        if not tienda:
            return Response({
                "Code": "Store_doesnt_exist",
                "Detailled": "Store doesn't exist in the data base",
                "Error": "La tienda no fue encontrada"
            }, status=status.HTTP_404_NOT_FOUND)

        if Oferta.objects.filter(name=request.data["name"], store=tienda):
            return Response({
                "Code": "Deal_already_exist",
                "Detailled": "Deal already exist in the data base",
                "Error": "La oferta ya existe en la base de datos"
            }, status=status.HTTP_409_CONFLICT)

        del request.data["store"]
        deal_pk = Oferta.objects.create(**request.data, store=tienda).pk

        return Response({
            "Code": "Inserted",
            "pk": deal_pk
        }, status=status.HTTP_201_CREATED)
