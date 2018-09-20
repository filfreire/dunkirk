from datetime import datetime
import logging
import sys
import os

log = logging.getLogger("textfile")


def generateBody(note):
    return "Imported from Apple Note\nOriginal Create Time: %s\nImport Time: %s\n-----------------------\n%s\n-----------------------\nhttps://github.com/adamyi/notes_to_keep\nhttps://github.com/filfreire/dunkirk" % (note.date_created.strftime("%c"), datetime.now().strftime("%c"), note.data.encode('utf-8'))

def writeNote(note, counter):
    filename = "temporary_export/note_" + str(counter) +".txt"
    log.info("Writing note: " + filename + " : " +  note.title.encode('utf-8'))
    text = generateBody(note)
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    f = open(filename , 'w')
    f.write(text)
    f.close()

def start(notes, num):

    if num != None:
        log.warning("As requested, we will only write %s note(s)." % num)
        num = int(num)
    i = 0

    for note in notes:
        try:
            i += 1
            writeNote(note, i)
            if i == num:
                break
        except Exception as e:
            log.error(e)
            if note.title is not None:
                log.error("Error parsing/updating this note... Skip this note for now. Title: " + note.title)
            continue
    log.info("Done! Have fun~")

if __name__ == '__main__':
    print "This is part of dunkirk, which cannot be called separately."
