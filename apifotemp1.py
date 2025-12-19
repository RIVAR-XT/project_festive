import requests

api_key = '5715eb7a-cf55-40cf-9136-5e0d6d4c34fd'
template_id = '0600b2d3-df5d-4792-9954-0b3de8c67026'

url = 'https://api.templated.io/v1/render'
headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {api_key}'
}

data = {
  'template': template_id,
  'layers': {
     
      'label-from' : {
        'text' : 'FROM:',
        'color' : 'rgba(69, 62, 62, 1)'
      },
      'line-from' : {
        
      },
      'label-to' : {
        'text' : 'TO:',
        'color' : 'rgba(69, 62, 62, 1)'
      },
      'line-to' : {
        
      },
      'christmas' : {
        'text' : 'Christmas!',
        'color' : 'rgba(225, 56, 50, 1)'
      },
      'merry' : {
        'text' : 'Merry',
        'color' : 'rgba(59, 105, 174, 1)'
      },
      'to' : {
        'text' : 'Dear Smith Family',
        'color' : 'rgba(69, 62, 62, 1)'
      },
      'from' : {
        'text' : 'The Johnson Family',
        'color' : 'rgba(69, 62, 62, 1)'
      }
  }
}



response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
  print('Render request accepted.')
  print(response.text)
  data = response.json()
  url = data.get("render_url")
  with open("file.jpg" , "wb" ) as f :
    f.write(requests.get(url).content)
else:
  print('Render request failed. Response code:', response.status_code)
  print(response.text)