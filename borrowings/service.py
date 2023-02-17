from django_filters import rest_framework as filters, BaseInFilter, BooleanFilter

from borrowings.models import Borrowing


class BorrowingFilter(filters.FilterSet):
    user_id = BaseInFilter(field_name="user_id")
    is_active = BooleanFilter(
        field_name="actual_return_date",
        lookup_expr="isnull",
        exclude=False
    )

    class Meta:
        model = Borrowing
        fields = ["is_active", "user_id"]
