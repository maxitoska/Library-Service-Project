from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from payment.models import Payment
from payment.serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
