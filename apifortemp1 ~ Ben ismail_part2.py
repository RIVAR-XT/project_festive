import requests
def first_api(sender_name , recipient_name , year ):
 api_key = '609256ac-746c-4801-9575-bff0fbcbfac6'
 template_id = '244d69fe-e186-40a9-8955-3187bb79a119'

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
        'text' : f'Dear {recipient_name}',
        'color' : 'rgba(69, 62, 62, 1)'
      },
      'from' : {
        'text' : f'{sender_name}',
        'color' : 'rgba(69, 62, 62, 1)'
      },
      'christmas-copy' : {
         'text' : f'{year}',
         'color' : 'rgba(225, 56, 50, 1)'
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


