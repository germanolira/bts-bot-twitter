import tweepy
import time
import os
import random
import glob
import shutil

CONSUMER_KEY = 'SUA CHAVE AQUI'
CONSUMER_SECRET = 'SUA CHAVE AQUI'
ACCESS_KEY = 'SUA CHAVE AQUI'
ACCESS_SECRET = 'SUA CHAVE AQUI'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

# Declara o PATH para pegar as imagens
# E usa random para escolher uma imagem aleatoria
# Passe o caminho da pasta dentro de r''
# Exemplo path = r'C:/User/Pasta'
path = r''
random_filename = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x)) and
    x.endswith('.png')
])
print(random_filename)
# Printa no console o nome do arquivo escolhido

# Usa o glob para copiar o arquivo escolhido aleatoriamente
# Da pasta img e copia para a pasta dst
src_dir = "./img"
dst_dir = "./post"
for pngfile in glob.iglob(os.path.join(src_dir, random_filename)):
    shutil.copy(pngfile, dst_dir)

# Lista todos os arquivos dentro de post
# E pega o ultimo arquivo modificado ou salvo
list_of_files = glob.glob('./post/*')
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)

# Carrega a imagem
imagePath = latest_file

# Envia o tweet
api.update_with_media(imagePath)
