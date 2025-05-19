import streamlit as st
from datetime import datetime, timedelta

# Aktuelle Minuszeit definieren
st.title("Arbeitszeit Tracking Tool")
minuszeit = st.number_input("Aktuelle Minuszeit (in Minuten):", value=556)

# Soll-Arbeitszeit festlegen (nicht bearbeitbar) sd
soll_arbeitszeit = datetime.strptime("08:24", "%H:%M").time()
st.markdown(f"**Tägliche Soll-Arbeitszeit:** {soll_arbeitszeit.hour:02d}:{soll_arbeitszeit.minute:02d}")

# Zeit und Pause-Eingaben
startzeit = st.time_input("Startzeit:")
endzeit = st.time_input("Endzeit:")
pause = st.number_input("Mittagspause (in Minuten):", value=60)

if st.button("Berechnen"):
    # Berechnung der tatsächlichen Arbeitszeit
    start = datetime.combine(datetime.today(), startzeit)
    end = datetime.combine(datetime.today(), endzeit)
    arbeitszeit = (end - start - timedelta(minutes=pause)).total_seconds() / 60
    soll_arbeitszeit_min = soll_arbeitszeit.hour * 60 + soll_arbeitszeit.minute
    tages_plus_minus = arbeitszeit - soll_arbeitszeit_min

    # Wöchentliches Plus/Minus berechnen
    wochen_plus_minus = tages_plus_minus * 4
    verbleibende_minuszeit = minuszeit - wochen_plus_minus

    # Ergebnisanzeige
    st.write(f"Tatsächliche Arbeitszeit: {arbeitszeit // 60:.0f} Stunden und {arbeitszeit % 60:.0f} Minuten")
    st.write(f"Tägliches Plus/Minus: {tages_plus_minus // 60:.0f} Stunden und {tages_plus_minus % 60:.0f} Minuten")
    st.write(f"Wöchentliches Plus/Minus: {wochen_plus_minus // 60:.0f} Stunden und {wochen_plus_minus % 60:.0f} Minuten")
    st.write(f"Verbleibende Minuszeit: {verbleibende_minuszeit // 60:.0f} Stunden und {verbleibende_minuszeit % 60:.0f} Minuten")

    # Fortschrittsanzeige
    wochen_benoetigt = verbleibende_minuszeit / wochen_plus_minus if wochen_plus_minus else float('inf')
    st.write(f"Zeit zum Ausgleich der Minuszeit: {wochen_benoetigt:.2f} Wochen")
