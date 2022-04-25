# Testprogramm-fuer-Manikin-WiFi-Library
Testprogramm für Manikin WiFi Library

start.bat startet die beiden Scripts TestClient.py und TestServer.py, sowie ein CMD-Fenster mit Netstat, zum überprüfen der TCP-Verbindung.
start.bat muss nicht als Administrator gestartet werden, das Script fragt engenständig nach Admin-Rechten.

Die jeweils vier letzten Bits jeder Sensornachricht werden randomisiert. Da ich nicht wusste, wie die übrigen Bits auszusehen haben, es nicht aus der Aufgabenstellung hervorging,
und ich im Internet keinen Standard finden konnte, habe ich die restlichen Bits auf 0 gesetzt. Andernfalls ließe sich das durch eine kleine Modifikation am Code ändern.

Da der Server den ansprüchen entsprechend alle 31 Nachrichten ein mal pro Sekunde sendet, muss der TestServer angehalten werden (bzw. das TestServer-Fenster geschlossen werden),
um alle 31 Nachrichten in Ruhe überprüfen zu können.
