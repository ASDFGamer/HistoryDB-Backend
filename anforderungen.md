# HistoryDB

Im folgenden soll eine Analyse der Idee eines Programms zur einfachen Anzeige von vielen verknpüften geschichtlichen Daten gemacht werden.

## Anforderungen

Folgene funktionale Anforderugen gibt es:

1. Anzeige von historischen Orten auf einer Karte
2. Anzeige von historischen Ereignissen in einem Zeitstrahl
3. Anzeige von detailierten Informationen zu Orten oder Ereignissen
4. Anzeige von Verknüpfungen zwischen verschiedenen Elementen (Orten oder Ereignissen)
5. Erweiterbarkeit um weitere Kategorien wie z.B. Personen oder Ländern
6. Gute Verknüpfung mit existierenden Diensten (z.B. Wikipedia)

Folgende nichtfunktionale Anforderungen gibt es:

1. Gutes Oberflächendesign
2. Verständliche Benutzerführung
3. Anzeige von Namen in verschiedenen Sprachen

Jede dieser Anforderungen soll im folgenden analysiert werden und dabei sollen alle möglichen Probleme herausgestellt werden.

Außerdem gibt es noch weiter nice-to-have Features die erstmal nicht implementiert werden sollen, aber schon im Design bedacht werden können:

1. Möglichkeit zum hinzufügen/korrigieren von Daten
2. Anzeige von historischen Personen
3. Anzeige von historischen Ländern
4. Anzeige von Kunstgegenständen 

## Anforderungsanalyse

### Anzeige von historischen Orten auf einer Karte

Für die Anzeige von historischen Orten müssen als erstes die Informationen zu den Daten beschafft werden. Hiernach müssen diese auf einer Karte dargestellt werden. Hierbei ist zu beachten, dass nicht zu viele angezeigt werden wenn die zoomstufe falsch gewählt ist.

### Anzeige von historischen Ereignissen in einem Zeitstrahl

Für die Anzeige von historischen Ereignissen müssen als erstes die Informationen zu den Ereignissen beschafft werden. Hiernach müssen diese auf einem Zeitstrahl oder einer anderen grafischen Darstellungsweise angezeigt werden. Hierbei ist zu beachten, dass für eine Zoomstufe nicht zu viele angezeigt werden.

### Anzeige von detailierten Informationen zu Orten oder Ereignissen

Für die Anzeige von detailierten Informationen sollen wenn möglich die Daten aus verschiedenen Quellen zusammengeführt werden. Außerdem sollen in der gleichen Ansicht auf die Verknüpfungen zu sehen sein.

### Anzeige von Verknüpfungen zwischen verscheiden Elementen

Für die Anzeige von Verknüpfungen zwischen verscheidenen Elementen müssen als erstes die Informationen für die Verknüpfungen beschafft werden. Hiernach müssen die sinnvoll sortiert werden, da es sehr viele Verknüpfungen geben kann. Von den Verküpfungen soll gleich auf die Detailseite des Verknüpften eintrags gesprungen werden.

### Gute verknüpfung zu existiereden Diensten
Für weitergehende Informationen soll auf existierende Dienste verwiesen werden. Diese sollen so eingebunden werden, dass es möglichst einfach ist dorthin zu wechseln.

### Weitere anforderungen

Die weiteren Anforerungen sind nicht technischer Natur und somit auf jeden Fall umsetzbar, auch wenn es dabei Probleme geben kann.

## Probleme

### Zusammenfassung der Probleme

Folgende Arten von Problemen wurden schon identifiziert:

1. Beschaffung der Datengrundlage
2. Gefilterte Anzeige der Daten je nach Zoomstufe
3. Erstellungen von Verknüpfungen zwischen Daten aus verschiedenen Quellen
4. Anzeige der Daten auf einer Karte

