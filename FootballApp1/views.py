from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from FootballApp1.forms import PlayerForm, TeamForm


def function_home(request):
    return HttpResponse('<h1>Hello world!</h1>')

def return_homepage(request):
   return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

from FootballApp1.models import Player
def players(request):
    if request.method == 'POST':
        # тут мы создаем новую задачу:
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            new_player = Player()
            # тут мы заполняем условие новой данными с сервера из формы:
            new_player.player_name = form.cleaned_data['player_name']
            new_player.player_dob = form.cleaned_data['player_dob']
            new_player.player_country = form.cleaned_data['player_country']
            new_player.player_curr_team_link = form.cleaned_data['player_curr_team_link']
            new_player.player_position = form.cleaned_data['player_position']
            new_player.player_photo = form.cleaned_data['player_photo']
            new_player.save()
        # теперь сохраняем нашу задачу в базу данных
    all_players = Player.objects.all() # вот эта строчка вытаскивает из базы данных все задачи
    player_form = PlayerForm()
    context = {'all_players': all_players, 'player_form': player_form}
    return render(request, 'players.html', context)


from FootballApp1.models import Team
def teams(request):
    if request.method == 'POST':
        # тут мы создаем новую задачу:
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            new_team = Team()
            # тут мы заполняем условие новой данными с сервера из формы:
            new_team.team_name = form.cleaned_data['team_name']
            new_team.stadium = form.cleaned_data['stadium']
            new_team.est_year = form.cleaned_data['est_year']
            new_team.curr_trainer = form.cleaned_data['curr_trainer']
            new_team.UEFA_rate = form.cleaned_data['UEFA_rate']
            new_team.emblem = form.cleaned_data['emblem']
            new_team.save()
        # теперь сохраняем нашу задачу в базу данных
    all_teams = Team.objects.all() # вот эта строчка вытаскивает из базы данных все задачи
    team_form = TeamForm()
    context = {'all_teams': all_teams, 'team_form': team_form}
    return render(request, 'teams.html', context)

