from textblob import TextBlob

eb = TextBlob('Hola amigos como estas?')
print(eb.translate(to='en'))