from django_filters import rest_framework as filters

from borrowings.models import Borrowing


class BaseInFilter(filters.BaseInFilter):
    pass


class BooleanInFilter(filters.BooleanFilter):
    pass


class BorrowingFilter(filters.FilterSet):
    user_id = BaseInFilter(field_name="user_id")
    is_active = BooleanInFilter(
        field_name="actual_return_date",
        lookup_expr="isnull",
        exclude=False
    )

    class Meta:
        model = Borrowing
        fields = ["is_active", "user_id"]
