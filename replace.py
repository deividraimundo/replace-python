import json

nome = 'estoque_20220930.json'

with open(nome) as infile:
  produtos = json.loads(infile.read())

for produto in produtos:
  data = f'{produto["date"]}'[:10]
  produto['date'] = produto['date'].replace(produto['date'], data)

with open(nome, 'w') as outfile:
  json.dump(produtos, outfile)
