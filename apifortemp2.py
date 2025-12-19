import requests

api_key = '5715eb7a-cf55-40cf-9136-5e0d6d4c34fd'
template_id = 'a496106a-61f5-49b6-be5a-bd755ba6165a'

url = 'https://api.templated.io/v1/render'
headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {api_key}'
}

data = {
  'template': template_id,
  'layers': {
      'subtitle' : {
        'text' : '&HAPPY NEW YEAR',
        'color' : 'rgba(255, 255, 255, 1)'
      },
      'title-christmas' : {
        'text' : 'Christmas',
        'color' : 'rgba(255, 255, 255, 1)'
      },
      'title-merry' : {
        'text' : 'MERRY',
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
      'to-line' : {
        
      },
      'from-line' : {
        
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
  print('Render request accepted.')
  print(response.text)
  data = response.json()
  url = data.get("render_url")
  with open("file.jpg" , "wb" ) as f :
    f.write(requests.get(url).content)
else:
  print('Render request failed. Response code:', response.status_code)
  print(response.text)