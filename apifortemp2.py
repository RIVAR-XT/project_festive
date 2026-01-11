
import requests





def second_api(sender_name , recipient_name , year):
  api_key = '609256ac-746c-4801-9575-bff0fbcbfac6'
  template_id = '6c65e8b2-b87e-4428-8e58-3e9ba827abd2'

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
        'text' : f"{recipient_name}",
        'color' : 'rgba(255, 255, 255, 1)'
      },
      'from' : {
        'text' : f"{sender_name}",
        'color' : 'rgba(255, 255, 255, 1)'
      },
      "subtitle-copy" : {
        "text" : f"{year}",
        "color" : "rgba(255, 255, 255, 1)"
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



