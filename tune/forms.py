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
        ]

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


class RepertoireTuneForm(ModelForm):
    class Meta:
        model = RepertoireTune
        exclude = ["tune", "player", "last_played", "started_learning"]


class SearchForm(forms.Form):
    TIMES = [
        ("anytime", "anytime"),
        ("day", "a day"),
        ("week", "a week"),
        ("month", "a month"),
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
        else:
            return None
