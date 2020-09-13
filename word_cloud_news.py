for index, row in df.iterrows():
    word = row['word']
    freq = row['freq']
    for (i in range(freq)):
        comment_words += " ".join(val) + " "

wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=10).generate(comment_words)

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig('xxxxxxxx.png')