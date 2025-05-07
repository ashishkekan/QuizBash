from django import forms

from .models import Choice


class QuestionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        choices = kwargs.pop("choices", None)
        super().__init__(*args, **kwargs)
        if choices is not None:
            self.fields["choice"] = forms.ModelChoiceField(
                queryset=choices,
                widget=forms.RadioSelect,
                empty_label=None,
                required=True,
                label="Select one option",
            )
