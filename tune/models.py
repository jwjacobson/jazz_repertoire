from django.db import models
from django.contrib.auth import get_user_model


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Tune(models.Model):
    """
    The Tune is the heart of this app; each tune is one song that can be added to a user's repertoire and should contain all relevant musical information.
    """

    METERS = [(3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, "7"), (0, "irregular")]

    STYLES = [("standard", "standard"), ("jazz", "jazz")]

    FORMS = [
        ("AABA", "AABA"),
        ("ABAC", "ABAC"),
        ("ABA", "ABA"),
        ("ABAB", "ABAB"),
        ("ABCD", "ABCD"),
        ("AB", "AB"),
        ("AAB", "AAB"),
        ("AABC", "AABC"),
        ("blues", "blues"),
        ("irregular", "irregular"),
    ]

    KEYS = {
        "c",
        "f",
        "bb",
        "eb",
        "ab",
        "db",
        "gb",
        "b",
        "e",
        "a",
        "d",
        "g",
        "a#",
        "d#",
        "g#",
        "c#",
        "f#",
        "c-",
        "f-",
        "bb-",
        "eb-",
        "ab-",
        "db-",
        "gb-",
        "b-",
        "e-",
        "a-",
        "d-",
        "g-",
        "a#-",
        "d#-",
        "g#-",
        "c#-",
        "f#-",
        "none",
        "atonal",
    }

    MAX_SEARCH_TERMS = 4

    NICKNAMES = {
        "bird": "Parker",
        "bud": "Powell",
        "miles": "Davis",
        "wayne": "Shorter",
        "joe": "Henderson",
        "lee": "Konitz",
        "diz": "Gillespie",
        "dizzy": "Gillespie",
        "duke": "Ellington",
        "sonny": "Rollins",
        "bill": "Evans",
        "herbie": "Hancock",
        "cedar": "Walton",
    }

    title = models.CharField(max_length=90, help_text="The only required field")
    composer = models.CharField(max_length=30, blank=True, help_text="Last names only for now")
    key = models.CharField(
        max_length=10,
        blank=True,
        help_text="Letters A-G, one only, add - for minor",
    )
    other_keys = models.CharField(
        max_length=20,
        blank=True,
        help_text="Letters A-G, as many as you want, separated by a space",
    )
    song_form = models.CharField(choices=FORMS, max_length=15, blank=True)
    style = models.CharField(choices=STYLES, max_length=15, blank=True, default="standard")
    meter = models.PositiveSmallIntegerField(choices=METERS, blank=True, null=True, default=4)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    is_contrafact = models.BooleanField(blank=True, null=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, blank=True, null=True
    )
    tags = models.ManyToManyField(
        Tag, related_name="tags", blank=True, help_text="(feature under construction)"
    )

    @property
    def decade(self):
        """
        Calculate the decade of composition based on the year of composition.
        """
        decade = f"{str(self.year)[2]}0s"
        return decade

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"Tune {self.id} | {self.title}"


class RepertoireTune(models.Model):
    """
    RepertoireTune is the ManyToMany table connecting tunes to users ("players").
    It holds lots of essential data about a player's relationship to the tune,
    such as when it was last played or how well they know it.
    """

    KNOWLEDGES = [("know", "know"), ("learning", "learning"), ("don't know", "don't know")]

    tune = models.ForeignKey(Tune, on_delete=models.CASCADE)
    player = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    last_played = models.DateField(blank=True, null=True)
    knowledge = models.CharField(choices=KNOWLEDGES, max_length=15, default="know", blank=True)
    started_learning = models.DateTimeField(blank=True, null=True)
    play_count = models.IntegerField(default=0)

    class Meta:
        unique_together = ("tune", "player")

    def __str__(self):
        return f"{self.tune} | {self.player}"
