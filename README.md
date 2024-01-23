# TESTING

Eine Komponente soll Daten aus einem CSV-File importieren und im XML-Format exportieren.

## Testideen

| Lazau Larissa | Postl Denise | 
|----------|----------|
| Check if file exists.   | UNIT Tests für die einzelnen Funktionen, um den richtigen OUTPUT zu garantieren. Testen der import Funktion & überprüfen ob der import richtig funktioniert. Testen der transform Funktion um zu überprüfen ob der richtige OUTPUT generiert wird. Testen der export Funktion um zu überprüfen ob der Inhalt auch wirklich exportiert wird in ein File.   |
| Check if import file is reading correctly.   | Integration Test um zu überprüfen, ob die verschiedenen Teile des Systems gut miteinander interagieren.   | 
| Transform. Fail when in import are no new data. Check Rows - CSV / XML. Fail Test: Check that XML is not empty  | End-to-End Test um den tatsächlichen Einsatz des Systems zu simulieren.    | 