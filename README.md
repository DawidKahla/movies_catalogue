# Biblioteka filmów

Aplikacja webowa pozwalająca wyświetlać pseudolosowe filmy z zadanej listy na podstawie danych z serwisu themoviedb.org. Po wejściu w "show more" prezentuje podstawowe informacje o filmie wraz z obsadą. 

W celu zapewnienia poprawnego działania aplikacji należy upewnić się, że na urządzeniu zainstalowane są wersje odpowiednich modułów, zgodnie z plikiem requirements.txt, co można zrobić przy pomocy polecenia: "pip install -r requirements.txt" Następnie należy wygenerować własny API_key ze strony https://developers.themoviedb.org/3/getting-started/introduction i stworzyć w katalogu z programem plik api_token.py zawierający kod:
def get_api_token():
    return "twój_indywidualny_api_key"

Aplikację można uruchomić poprzez uruchomienie pliku start.bat i wpisanie "http://127.0.0.1:5000/" w adres dowolnej przeglądarki internetowej.