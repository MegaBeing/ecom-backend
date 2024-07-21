from django.contrib.admin import SimpleListFilter
from django.utils.translation import gettext_lazy as _

class IntegerRangeFilter(SimpleListFilter):
    title = _('price')
    parameter_name = 'range'

    def lookups(self, request, model_admin):
        return (
            ('0-500', _('Less Than 500')),
            ('501-1000', _('501 to 1000')),
            ('1001-3000', _('1001 to 3000')),
            ('>3000',_('Above 3000'))
            # Add more ranges as needed
        )

    def queryset(self, request, queryset):
        if self.value() == '0-500':
            return queryset.filter(price__gte=0, price__lte=500)
        if self.value() == '501-1000':
            return queryset.filter(price__gte=501, price__lte=1000)
        if self.value() == '1001-2000':
            return queryset.filter(price__gte=1001, price__lte=3000)
        if self.value() == '>3000':
            return queryset.filter(price__gte=3001)
        # Add more ranges as needed
        return queryset