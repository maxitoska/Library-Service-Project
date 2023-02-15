from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

from books.permissions import IsAdminOrIfAuthenticatedReadOnly
from borrowings.models import Borrowing
from borrowings.serializers import (
    BorrowingSerializer,
    BorrowingCreateSerializer,
    BorrowingListSerializer,
    BorrowingDetailSerializer,
    BorrowingReturnSerializer,

)


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    # def create(self, request, *args, **kwargs):
    #     some_data = {"user_id": self.request.user.id, **request.data}
    #     serializer = self.serializer_class(data=some_data)
    #     serializer.is_valid(raise_exception=True)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if self.action == "list":
            return BorrowingListSerializer
        if self.action == "retrieve":
            return BorrowingDetailSerializer
        if self.action == "create":
            return BorrowingCreateSerializer
        if self.action == "return_book":
            return BorrowingReturnSerializer
        return BorrowingSerializer

    @action(detail=True, methods=['patch'], url_path="return")
    def return_book(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.update(instance, request.data)
        return Response(BorrowingSerializer(instance).data, status=status.HTTP_200_OK)



# class UserAdminsViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.filter(borrowings__is_active=True).select_related("borrowings")
#     serializer_class = UserSerializer
#     permission_classes = (IsAdminUser,)
