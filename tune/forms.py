from django.forms import ModelForm
from django import forms
from .models import Tune, RepertoireTune
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.utils import timezone
from datetime import timedelta


class TuneForm(ModelForm):
    class Meta:
        model = Tune
        fields = [
            "title",
            "composer",
            "key",
            "other_keys",
            "song_form",
            "style",
            "meter",
            "year",
            # "tags",
        ]

    def __init__(self, *args, **kwargs):
        super(TuneForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"

    def clean_key(self):
        """
        Check if the key entered is a real key and raise a ValidationError if it is not;
        Properly format the key (title case)
        """
        data = self.cleaned_data["key"]
        if data and data.lower() not in Tune.KEYS:
            raise ValidationError(
                {_('Invalid key (all normal keys accepted plus "none" and "atonal").')}
            )
        return data.title()

    def clean_other_keys(self):
        """
        Check if the other keys entered are real keys and raise ValidationErrors if they are not;
        Properly format the keys (title case)
        """
        data = self.cleaned_data["other_keys"]
        if data is None:
            return data
        formatted_data = []
        for other_key in data.split():
            if other_key.lower() not in Tune.KEYS:
                raise ValidationError(_(f'"{other_key}" is not a valid key.'))
            formatted_data.append(other_key.title())
        data = " ".join(formatted_data)
        return data

    # def clean_tags(self):
    #     data = self.cleaned_data["tags"]
    #     if data is None:
    #         return data
    #     formatted_data = []
    #     for tag in data.split():
    #         formatted_data.append(tag.lower())
    #     data = " ".join(formatted_data)
    #     return data


class DateInput(forms.DateInput):
    input_type = "date"


class RepertoireTuneForm(ModelForm):
    class Meta:
        model = RepertoireTune
        exclude = ["tune", "player", "started_learning", "play_count"]
        widgets = {"last_played": DateInput()}

    def __init__(self, *args, **kwargs):
        super(RepertoireTuneForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class SearchForm(forms.Form):
    TIMES = [
        ("anytime", "anytime"),
        ("day", "a day"),
        ("week", "a week"),
        ("month", "a month"),
        ("two_months", "2 months"),
        ("three_months", "3 months"),
    ]

    search_term = forms.CharField(label="search_term", max_length=200, required=False)
    timespan = forms.ChoiceField(choices=TIMES, required=False)

    def clean_timespan(self):
        timespan = self.cleaned_data["timespan"]
        if timespan == "day":
            return timezone.now() - timedelta(days=1)
        elif timespan == "week":
            return timezone.now() - timedelta(days=7)
        elif timespan == "month":
            return timezone.now() - timedelta(days=30)
        elif timespan == "two_months":
            return timezone.now() - timedelta(days=60)
        elif timespan == "three_months":
            return timezone.now() - timedelta(days=90)
        else:
            return None
