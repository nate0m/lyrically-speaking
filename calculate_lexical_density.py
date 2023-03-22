from flask import Flask, request, render_template
import lyricsgenius
from lexicalrichness import LexicalRichness

genius = lyricsgenius.Genius("eCtt4Ho3HIa0j6ZSEw6hA9gkfKQfXa7eEV0GYp_gAYRmTrW-KS-3xoHBMwPUiGsv")

app = Flask(__name__)

@app.route('/calc_lexical_density', methods=['GET', 'POST'])
def calculate_lexical_density():
    if request.method == 'POST':
        artist1 = request.form['artist1']
        artist2 = request.form['artist2']
        song1 = request.form['song1']
        song2 = request.form['song2']

        # Searching songs using lyricsgenius library
        search1 = genius.search_song(song1, artist1)
        search2 = genius.search_song(song2, artist2)

        # Retrieve lyrics using lyricsgenius library
        lyrics1 = search1.lyrics
        lyrics2 = search2.lyrics

        # Retrieve annotations count using lyricsgenius library
        annotations1 = search1.annotation_count
        annotations2 = search2.annotation_count

        # Retrieve song art using lyricsgenius library
        song1_art = search1.song_art_image_url
        song2_art = search2.song_art_image_url

        print(song1_art)
        # Calculate lexical density using lexicalrichness library
        lex1 = LexicalRichness(lyrics1)
        lex2 = LexicalRichness(lyrics2)
        # density1 = lex1.ttr
        # density1 = '{:.2f}'.format(calc_dens1)
        # density2  = lex2.ttr
        # density2 = '{:.2f}'.format(calc_dens2)

        # print(density1)
        #  print(density2)

        # need to figure out how to display graph of lexical density
        # print(lex1.vocd_fig(ntokens=50, within_sample=100, seed=42))

        # returning different lexical density calculations using lex objects and lexicalrichness library methods
        # it would be cool to have a small amount of the lyrics displyed and on click the lyrics would expand to show all of them
        return render_template('results.html',
                               ttr1=lex1.ttr, ttr2=lex2.ttr,
                               vocd1=lex1.vocd(ntokens=50, within_sample=100, iterations=3), vocd2=lex2.vocd(ntokens=50, within_sample=100, iterations=3),
                               mattr1=lex1.mattr(window_size=25), mattr2=lex2.mattr(window_size=25),
                               a1=annotations1, a2=annotations2,
                               artist1=artist1, artist2=artist2,
                               song1_art=song1_art, song2_art=song2_art,
                               song1=song1, song2=song2)
    else:
        return render_template('index.html')




