# Guess The Number 2

Proste okno które losuje liczbe i daje 5 tur w których można ją zgadnąć.

## Setup

### Dla Windowsa
Trzeba zainstalować bibliotekę `pillow`. Można to zrobić w terminalu uruchamiając komendę:

```ps
python -m pip install pillow
```

Jeżeli gra dalej nie działa i skarży się o brakujące biblioteki, można je zainstalować komendą:

```ps
python -m pip install [NAZWA BIBLIOTEKI]
```

### Dla Linuxa
Szczerze nie wiem co trzeba. Wiem, że dla mnie trzeba było zainstalować paczkę systemową `tk`. A tak to pillow działał.

Jeżeli gra dalej nie działa i skarży się o brakujące biblioteki, to trzeba wyszukać jak je zainstalować dla swojej dystrybucji.

## Problemy z wersją na UPEL

W jednym miejscu zamiast górnego zakresu zgadywanej liczby 50 jest napisane 20, co sprawia, że nie da się zgadnąć liczby wyższej niż 20.
