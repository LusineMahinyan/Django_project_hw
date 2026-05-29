from django import forms

from catalog.models import Product
from catalog.constants import FORBIDDEN_WORDS


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():

            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"

    def clean_price(self):

        price = self.cleaned_data.get("price")

        if price < 0:
            raise forms.ValidationError(
                "Цена не может быть отрицательной."
            )

        return price

    def clean(self):

        cleaned_data = super().clean()

        name = cleaned_data.get("name", "").lower()
        description = cleaned_data.get("description", "").lower()

        for word in FORBIDDEN_WORDS:

            if word in name:
                self.add_error(
                    "name",
                    f'Запрещено использовать слово "{word}"'
                )

            if word in description:
                self.add_error(
                    "description",
                    f'Запрещено использовать слово "{word}"'
                )

        return cleaned_data
