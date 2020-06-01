from django import forms
from FootballApp1.models import Player, Team


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player  # для какой модели будет создана форма
        fields = ['player_name', 'player_dob', 'player_country', 'player_curr_team_link', 'player_position', 'player_photo']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team  # для какой модели будет создана форма
        fields = ['team_name', 'stadium', 'est_year', 'curr_trainer', 'UEFA_rate', 'emblem']