notes = [
    {"title": "Einkauf", "text": "Milch, Brot, Eier"},
    {"title": "Arbeit", "text": "Backendcall um 11"},
]

def show_notes():
    for note in notes:
        print(f"\nTitle: {note['title']}, Text: {note['text']}")
    
    

def add_note():
    title = input("\nTitel: ")
    text = input("Text: ")

    notes.append({
        "title": title,
        "text": text
    })

    print("\nIhre neue Notiz wurde hinzugefügt :)\n")

    show_notes()
    

def delete_note():
    show_notes()
    num = int(input("\nWelchen eintrag möchten sie Löschen? geben sei einen Index ein satrt sie bei 0 für den Ersten Eintrag\n"))

    print(num)
    del notes[num]

    print("\nEintrag erfolgreich gelöscht.\n")
    show_notes()
   

def update_note():
    anzahl = len(notes)
    show_notes()
    index = int(input(f"\nWelchen eintrag möchten sie Aktualisieren? Wählen sie eine Zahl zwischen 0 - {anzahl - 1}\n"))

    neuer_titel = input("Neuer Titel: ")
    neuer_text = input("Neuer Text: ")

    notes[index]["title"] = neuer_titel
    notes[index]["text"] = neuer_text

    print("\nEintag erfolgreich Aktualisiert!\n")
    show_notes()


    

def abfrage():
    print("\nTreffen sie eine Auswahl.")
    while True:
        coicenum = int(input(
            "\n1 Alle Notes anzeigen"
            "\n2 Neue Note"
            "\n3 Note aktualisieren"
            "\n4 Note löschen"
            "\n5 Beenden\n"
        ))

        match coicenum:
            case 1:
                show_notes()

            case 2:
                add_note()

            case 3:
                update_note()

            case 4:
                delete_note()

            case 5:
                break




abfrage()


