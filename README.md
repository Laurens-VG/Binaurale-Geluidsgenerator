# Project Biomedische: Binaural Audio
In dit project wordt het geluid van een wav file omgezet naar een binaural
gegenereerd geluid dat afhankelijk is van de plaats waar een persoon zich bevindt aan de webcam.
De parameters kunnen ook via een RPi handmatig worden ingesteld.


Universiteit Gent \
Faculteit Ingenieurswetenschappen en architectuur \
Opleiding Industriële Wetenschappen Elektronica-ICT \
Academiejaar 2019-2020

Auteurs: Stephanie Maes, Laurens Van Goethem, Reiner De Smet, Lander T'Kindt \
Project onder begeleiding van: Prof.  dr. ir. Paul Devos 
Algemeen begeleider:  Ing.  Matthias De Schepper

## Inhoud

- **sounds**: dataset van verschillende geluiden
- **main.py**: hoofdbestand om een Tetris bestand binaural te genereren
- **parameters.py**: bestand dat de parameterwaarden berekend
- **split_sound.py**: bestand dat de het geluid splitst in kanalen
- **input_binaural.py**: bestand dat de parameterwaarden toepast op de kanalen
- **headtracking_distance.py**: bestand dat de parameterwaarden via de webcam bepaalt
- **haarcascade_frontalface_default.xml**: bestand dat de nodig is voor de webcam te activeren
- **rotary.py**: bestand dat de parameterwaarden van de Raspberry Pi leest
- **pot.py**: bestand dat de parameterwaarden van de potentiometers verstuurt.


## Gebruik

Het project gebruikt python 3.7 \
De packages (zie versie controle) kunnen geïnstalleerd worden met pip:

    pip install -r requirements.txt
    
**Main.py**

Hoofdbestand om een Tetris.wav af te spelen met de toegepaste methoden. Voor het runnen is het nodig om 
in headtracking_distance.py de gebruikersnaam op te geven in de variabele naam.

gebruik:

    python main.py
    
    
## Versie controle

OS: Windows 10

IDE: JetBrains Pycharm 2019.2.2 (Professional Edition)

Python 3.7.1

Packages
- pydub
- pygame
- matplotlib
- numpy
- scipy
- wave
- opencv-python

