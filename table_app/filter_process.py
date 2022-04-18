from .models import TableData
from .forms import FilterForm, SortForm


class FilterProcess:
    def __init__(self, filters: FilterForm, sorting: SortForm):
        self.filters = filters
        self.sorting = sorting

    @property
    def get_data(self):
        table = TableData.objects.all()
        if self.filters.is_valid():
            categories = self.filters.cleaned_data["categories"]
            condition = self.filters.cleaned_data["condition"]
            choose = self.filters.cleaned_data["choose"]

            match categories:
                case 'title':
                    if condition == 'contains':
                        table = table.filter(title__contains=choose)
                    # elif condition == 'equal':
                    #     table = table.filter(quantity=choose)
                case 'quantity':
                    match condition:
                        case 'contains':
                            table = table.filter(quantity__contains=choose)
                        case 'equal':
                            table = table.filter(quantity=choose)
                        case 'gt':
                            table = table.filter(quantity__gt=choose)
                        case 'lt':
                            table = table.filter(quantity__lt=choose)
                case 'distance':
                    match condition:
                        case 'contains':
                            table = table.filter(quantity__contains=choose)
                        case 'gt':
                            table = table.filter(distance__gt=choose)
                        case 'lt':
                            table = table.filter(distance__lt=choose)
                        case 'equal':
                            table = table.filter(distance=choose)
        if self.sorting.is_valid():
            sorting = self.sorting.cleaned_data["sorting"]
            if sorting:
                table = table.order_by(sorting)
            if sorting == '------':
                table = table.order_by(sorting)
        return table
