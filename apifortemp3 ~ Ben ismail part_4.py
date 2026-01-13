import requests

def third_api(sender_name , recipient_name , year):
    api_key = '609256ac-746c-4801-9575-bff0fbcbfac6'
    template_id = '3e09ed3e-d8eb-44b1-929d-20796bc8eecf'

    url = 'https://api.templated.io/v1/render'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    data = {
        'template': template_id,
        'layers': {
            'merry': {
                'text': 'Merry',
                'color': 'rgba(255, 255, 255, 1)'
            },
            'christmas': {
                'text': 'Christmas!',
                'color': 'rgba(255, 255, 255, 1)'
            },
            'label-to': {
                'text': 'To:',
                'color': 'rgba(255, 255, 255, 1)'
            },
            'label-from': {
                'text': 'From:',
                'color': 'rgba(255, 255, 255, 1)'
            },
            'line-to': {
            },
            'line-from': {
            },
            'divider': {
            },
            'to': {
                'text': f"{recipient_name}",
                'color': 'rgba(255, 255, 255, 1)'
            },
            'from': {
                'text': f"{sender_name}",
                'color': 'rgba(255, 255, 255, 1)'
            },
            "christmas-copy" : {
               "text" : f"{year}",
                "color" : "rgba(255, 255, 255, 1)"
            }
        }
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print('Render request accepted.')
        print(response.text)
        data = response.json()
        url = data.get("render_url")
        with open("file.jpg", "wb") as f:
            f.write(requests.get(url).content)
    else:
        print('Render request failed. Response code:', response.status_code)
        print(response.text)

