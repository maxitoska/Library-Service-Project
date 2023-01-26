from django.urls import path, include
from rest_framework import routers

from borrowings.views import BorrowingViewSet, BorrowingReturnView

router = routers.DefaultRouter()
router.register("borrowings", BorrowingViewSet)

urlpatterns = [

    path("", include(router.urls)),
    path("borrowings/<int:pk>/return/", BorrowingReturnView.as_view({'get': 'list'}), name="borrowing_return")

    ]

app_name = "borrowings"
