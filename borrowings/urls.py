from django.urls import path, include

from rest_framework import routers

from borrowings.views import BorrowingViewSet, BorrowingReturnView, UserAdminsViewSet

router = routers.DefaultRouter()
router.register("borrowings", BorrowingViewSet)

urlpatterns = [

    path("", include(router.urls)),
    path(
        "borrowings/<int:pk>/return/",
        BorrowingReturnView.as_view({'patch': 'partial_update'}),
        name="borrowing_return"
    ),
    path(
        "borrowings/?/return/",
        UserAdminsViewSet.as_view({'post': 'create'}),
        name="active_borrowing"
    ),
]

app_name = "borrowings"
