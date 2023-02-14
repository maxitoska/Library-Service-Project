from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser
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
from user.models import User
from user.serializers import UserSerializer


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def create(self, request, *args, **kwargs):
        some_data = {"user_id": self.request.user.id, **request.data}
        serializer = self.serializer_class(data=some_data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if self.action == "list":
            return BorrowingListSerializer
        if self.action == "retrieve":
            return BorrowingDetailSerializer
        if self.action == "create":
            return BorrowingCreateSerializer

        return BorrowingSerializer


class BorrowingReturnViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingReturnSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    # def get_serializer_class(self):
    #     if self.action == "partial_update":
    #         return BorrowingReturnSerializer
    #
    #     return BorrowingSerializer


# class UserAdminsViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.filter(borrowings__is_active=True).select_related("borrowings")
#     serializer_class = UserSerializer
#     permission_classes = (IsAdminUser,)

