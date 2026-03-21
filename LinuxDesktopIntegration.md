
Öffne dein Terminal (Strg + Alt + T).
Erstelle eine neue Datei mit diesem Befehl:
nano ~/.local/share/applications/obsidian.desktop
Kopiere diesen Text hinein (Pfade eventuell anpassen, falls dein Ordner anders heißt):
Ini, TOML

[Desktop Entry]
Name=Obsidian
Exec=/home/DEIN_NUTZERNAME/Programme/Obsidian-1.x.x.AppImage
Terminal=false
Type=Application
Icon=obsidian
Categories=Office;TextEditor;

(Ersetze DEIN_NUTZERNAME durch deinen echten Usernamen und achte auf den exakten Dateinamen der AppImage-Datei!)

Speichere mit Strg + O, Bestätige mit Enter und schließe mit Strg + X.