# Sports App

Školní aplikace pro domlouvání sportovních aktivit.

## První funkční demo

Na počítači vytvoříme nebo změníme sportovní událost.
Telefon ji načte přes síť a po obnovení stránky zobrazí změnu.

## Jak demo spustit

Všechny příkazy zadáváme v Terminálu z hlavní složky projektu.

1. Vytvoříme událost:
   python3 server/main.py

2. Spustíme server a necháme ho běžet:
   python3 -m http.server 8000 --bind 0.0.0.0 --directory server

3. Na telefonu otevřeme:
   http://IP_ADRESA_POCITACE:8000/event.json

IP_ADRESA_POCITACE nahradíme skutečnou IP adresou počítače.
Zařízení musí být v síti, která dovoluje jejich vzájemné spojení.

## Jak ukázat změnu

V dalším okně Terminálu přejdeme do hlavní složky projektu.
Spustíme python3 server/main.py a zadáme jinou kapacitu.
Na telefonu obnovíme stránku. Zobrazí se nová hodnota.

## Co zatím demo neumí

Uchovává pouze jednu událost. Další zadání ji přepíše.
Změny se zobrazí až po ručním obnovení stránky.
Zatím nemáme účty ani samostatné mobilní aplikace.