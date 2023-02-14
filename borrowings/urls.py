from django.urls import path, include

from rest_framework import routers

from borrowings.views import BorrowingViewSet, BorrowingReturnViewSet  # UserAdminsViewSet

router = routers.DefaultRouter()
router.register("borrowings", BorrowingViewSet)

urlpatterns = [

    path("", include(router.urls)),
    path(
        "borrowings/<int:pk>/return/",
        BorrowingReturnViewSet.as_view({'get': 'list'}),
        name="borrowing_return"
    ),
    # path(
    #     "borrowings/?/return/",
    #     UserAdminsViewSet.as_view({'post': 'create'}),
    #     name="active_borrowing"
    # ),
]

app_name = "borrowings"
