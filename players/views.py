from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import requests
from django.http import JsonResponse
from django.views import View

# Create your views here.
def base(request):
    return render(request, 'players.html')

# class HighScoresView(View):
#     def get(self, request):
#         api_base_urls = ["https://api.tibiadata.com/v3/highscores/Collabra/experience/all/", "https://api.tibiadata.com/v3/highscores/Ustebra/experience/all/"]
#         headers = {"accept": "application/json"}

#         all_highscores = []  # Lista para armazenar todos os dados dos highscores

#         for api_base_url in api_base_urls:
#             highscores_data = []  # Lista para armazenar os dados de uma única API

#             for page_number in range(1, 21):  # Loop de 1 a 20
#                 api_url = f"{api_base_url}{page_number}"  # Gere a URL com base no número da página

#                 try:
#                     response = requests.get(api_url, headers=headers)
#                     response.raise_for_status()  # Verifica se a solicitação foi bem-sucedida

#                     json_data = response.json()  # Converte a resposta JSON em um dicionário Python

#                     # Adicione os dados da página atual à lista dos highscores de uma única API
#                     highscores_data.append(json_data['highscores'])
#                 except requests.exceptions.RequestException as e:
#                     return render(request, 'erro.html', {'error_message': 'Erro ao fazer a solicitação à API'})

#             all_highscores.append(highscores_data)  # Adicione os highscores de uma única API à lista geral

#         return render(request, 'players.html', {'all_highscores': all_highscores})
class HighScoresView(View):
    def get(self, request):
        api_base_urls = ["https://api.tibiadata.com/v3/highscores/Collabra/experience/all/", "https://api.tibiadata.com/v3/highscores/Ustebra/experience/all/"]
        headers = {"accept": "application/json"}

        all_highscores = []  # Lista para armazenar todos os dados dos highscores

        for api_base_url in api_base_urls:
            highscores_data = []  # Lista para armazenar os dados de uma única API

            for page_number in range(1, 21):  # Loop de 1 a 20
                api_url = f"{api_base_url}{page_number}"  # Gere a URL com base no número da página

                try:
                    response = requests.get(api_url, headers=headers)
                    response.raise_for_status()  # Verifica se a solicitação foi bem-sucedida

                    json_data = response.json()  # Converte a resposta JSON em um dicionário Python

                    # Adicione os dados da página atual à lista dos highscores de uma única API
                    highscores_data.append(json_data['highscores'])
                except requests.exceptions.RequestException as e:
                    return render(request, 'erro.html', {'error_message': 'Erro ao fazer a solicitação à API'})

            all_highscores.append(highscores_data)  # Adicione os highscores de uma única API à lista geral

  # Inicializa as variáveis de contagem
        corporation_count_collabra = 0
        corporation_count_ustebra = 0

        for player in all_highscores[0]:
            for data in player.get('highscore_list', []):
                if "corporation" in data.get('name', '').lower():
                    corporation_count_collabra += 1

        for player in all_highscores[1]:
            for data in player.get('highscore_list', []):
                if "corporation" in data.get('name', '').lower():
                    corporation_count_ustebra += 1

        return render(request, 'players.html', {
            'all_highscores': all_highscores,
            'corporation_count_collabra': corporation_count_collabra,
            'corporation_count_ustebra': corporation_count_ustebra
        })