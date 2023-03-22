#!/usr/bin/env python3
import cgi
import subprocess
import lyricsgenius
from lexicalrichness import LexicalRichness

genius = lyricsgenius.Genius("eCtt4Ho3HIa0j6ZSEw6hA9gkfKQfXa7eEV0GYp_gAYRmTrW-KS-3xoHBMwPUiGsv")

def calculate_ld(artist, song):
    song = genius.search_song(artist, song)
    lex = LexicalRichness(song.lyrics)
    return lex.terms/lex.words

print("Content-type: text/html")
print()

form = cgi.FieldStorage()
song1 = form.getfirst("song1", "")
artist1 = form.getfirst("artist1", "")
song2 = form.getfirst("song2", "")
artist2 = form.getfirst("artist2", "")


# Call your existing Python program to calculate lexical density for each song
ld1 = calculate_ld(artist1, song1)
ld2 = calculate_ld(artist2, song2)

# Generate HTML page with result
print("<html><body>")
print(f"<p>Lexical density for {song1} by {artist1}: {ld1}</p>")
print(f"<p>Lexical density for {song2} by {artist2}: {ld2}</p>")
if ld1 > ld2:
    print(f"<p>{song1} by {artist1} has greater lexical density.</p>")
elif ld2 > ld1:
    print(f"<p>{song2} by {artist2} has greater lexical density.</p>")
else:
    print("<p>The songs have the same lexical density.</p>")
print("</body></html>")

