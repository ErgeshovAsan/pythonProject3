from decouple import Config, RepositoryIni
from logic import play_game

def main():
    config = Config(RepositoryIni('./settings.ini'))
    min_number = config('min_number', cast=int, default=1)
    max_number = config('max_number', cast=int, default=100)
    attempts = config('attempts', cast=int, default=5)
    initial_capital = config('initial_capital', cast=int, default=100)
    play_game(min_number, max_number, attempts, initial_capital)

if __name__ == "__main__":
    main()