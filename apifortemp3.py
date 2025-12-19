import requests

api_key = '5715eb7a-cf55-40cf-9136-5e0d6d4c34fd'
template_id = 'ef25e2d4-f369-44a1-9789-dc7ec730b407'

url = 'https://api.templated.io/v1/render'
headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {api_key}'
}

data = {
  'template': template_id,
  'layers': {
      'patern' : {
        'image_url' : 'https://picsum.photos/200/300.jpg'
      },
      'image-tree' : {
        'image_url' : 'https://picsum.photos/200/300.jpg'
      },
      'merry' : {
        'text' : 'Merry',
        'color' : 'rgba(255, 255, 255, 1)'
      },
      'christmas' : {
        'text' : 'Christmas!',
        'color' : 'rgba(255, 255, 255, 1)'
      },
      'label-to' : {
        'text' : 'To:',
        'color' : 'rgba(255, 255, 255, 1)'
      },
      'label-from' : {
        'text' : 'From:',
        'color' : 'rgba(255, 255, 255, 1)'
      },
      'line-to' : {
        
      },
      'line-from' : {
        
      },
      'divider' : {
        
      },
      'to' : {
        'text' : 'Dear Smith Family',
        'color' : 'rgba(255, 255, 255, 1)'
      },
      'from' : {
        'text' : 'The Johnson Family',
        'color' : 'rgba(255, 255, 255, 1)'
      }
  }
}

import requests

api_key = '5715eb7a-cf55-40cf-9136-5e0d6d4c34fd'
template_id = 'ef25e2d4-f369-44a1-9789-dc7ec730b407'

url = 'https://api.templated.io/v1/render'
headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {api_key}'
}

data = {
  'template': template_id,
  'layers': {
      'merry' : {
        'text' : 'Merry',
        'color' : 'rgba(255, 255, 255, 1)'
      },
      'christmas' : {
        'text' : 'Christmas!',
        'color' : 'rgba(255, 255, 255, 1)'
      },
      'label-to' : {
        'text' : 'To:',
        'color' : 'rgba(255, 255, 255, 1)'
      },
      'label-from' : {
        'text' : 'From:',
        'color' : 'rgba(255, 255, 255, 1)'
      },
      'line-to' : {
        
      },
      'line-from' : {
        
      },
      'divider' : {
        
      },
      'to' : {
        'text' : 'Dear Smith Family',
        'color' : 'rgba(255, 255, 255, 1)'
      },
      'from' : {
        'text' : 'The Johnson Family',
        'color' : 'rgba(255, 255, 255, 1)'
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