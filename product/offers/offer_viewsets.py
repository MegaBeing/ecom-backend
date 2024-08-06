from rest_framework import viewsets,permissions
from .offer_models import Offer
from .offer_serializers import OfferSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class OfferViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.AllowAny]
    
    @action(detail=False, methods=['GET'],url_path='images')
    def offer_images(self, request):
        queryset = self.queryset.filter(is_active=True)
        response = list()
        for offer in queryset:
            image_url = request.build_absolute_uri(offer.image.url)
            response.append({'id': offer.id, 'image': image_url})
        return Response(response)