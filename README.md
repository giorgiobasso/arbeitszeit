# Arbeitszeit Tracking Tool

Dieses Streamlit-basierte Tool ermöglicht es dir, deine tägliche Arbeitszeit zu erfassen und dein aktuelles Zeitguthaben (Plus/Minus) zu verfolgen.

## Funktionen

* **Eingabe der aktuellen Minuszeit:** Du kannst deine bestehende Minusstunden eingeben, um diese in die Berechnungen einzubeziehen.
* **Vordefinierte Soll-Arbeitszeit:** Die tägliche Soll-Arbeitszeit ist fest auf 8 Stunden und 24 Minuten eingestellt.
* **Start- und Endzeit-Eingabe:** Gib einfach deine tatsächliche Arbeitszeit über intuitive Zeitwahlfelder ein.
* **Pausenzeit-Eingabe:** Erfasse deine Mittagspause in Minuten.
* **Automatische Berechnung:** Nach Eingabe aller Daten und Klicken auf "Berechnen" werden folgende Werte automatisch ermittelt:
    * **Tatsächliche Arbeitszeit:** Die effektiv gearbeitete Zeit nach Abzug der Pause.
    * **Tägliches Plus/Minus:** Die Differenz zwischen deiner tatsächlichen Arbeitszeit und der Soll-Arbeitszeit.
    * **Wöchentliches Plus/Minus:** Eine Hochrechnung deines täglichen Plus/Minus auf eine 4-Tage-Woche (basierend auf der Annahme, dass die eingegebene Arbeitszeit einem von vier Arbeitstagen entspricht).
    * **Verbleibende Minuszeit:** Deine ursprüngliche Minuszeit abzüglich des heutigen Tagesgewinns (oder zuzüglich des Verlusts).
    * **Zeit zum Ausgleich der Minuszeit:** Eine Schätzung, wie viele Wochen du bei gleichbleibendem täglichen Plus/Minus benötigen würdest, um deine aktuelle Minuszeit auszugleichen.

## Anwendung

### Voraussetzungen

* **Python 3.6+** ist auf deinem System installiert.
* **pip** (Python Package Installer) ist installiert.

### Installation

1.  **Klone das Repository** (oder lade die `arbeitszeit_tracker.py`-Datei herunter):
    ```bash
    git clone <repository-url>
    cd <repository-ordner>
    ```
    (Ersetze `<repository-url>` durch die tatsächliche URL des GitHub-Repositorys und `<repository-ordner>` durch den Namen des Ordners.)

2.  **Installiere die benötigten Python-Bibliotheken:**
    ```bash
    pip install streamlit
    ```

### Ausführen des Tools

1.  **Navigiere im Terminal** zu dem Ordner, in dem sich die `arbeitszeit_tracker.py`-Datei befindet.

2.  **Führe Streamlit aus:**
    ```bash
    streamlit run arbeitszeit_tracker.py
    ```

3.  **Das Tool öffnet sich automatisch** in deinem Standard-Webbrowser.

### Bedienung

1.  **Gib deine aktuelle Minuszeit** im dafür vorgesehenen Feld ein (falls zutreffend).
2.  Die **tägliche Soll-Arbeitszeit** von 08:24 wird angezeigt und ist nicht bearbeitbar.
3.  Wähle deine **Startzeit** und **Endzeit** über die Zeitwahlfelder aus.
4.  Gib die Dauer deiner **Mittagspause** in Minuten ein.
5.  Klicke auf den Button **"Berechnen"**.
6.  Die **Ergebnisse** deiner Arbeitszeitberechnung werden unter dem Button angezeigt, einschließlich der tatsächlichen Arbeitszeit, des täglichen und wöchentlichen Plus/Minus, der verbleibenden Minuszeit und einer Schätzung der benötigten Zeit zum Ausgleich der Minuszeit.

## Hinweise

* Die Berechnung des wöchentlichen Plus/Minus basiert auf der Annahme einer 4-Tage-Woche und dass die eingegebene Arbeitszeit einem dieser Tage entspricht.
* Die Schätzung der Zeit zum Ausgleich der Minuszeit ist eine grobe Annäherung und berücksichtigt keine zukünftigen Schwankungen deiner Arbeitszeiten.
* Dieses Tool dient zur persönlichen Zeiterfassung und ersetzt keine offizielle Arbeitszeiterfassungssysteme.

## Autor

[Giorgio Basso]
