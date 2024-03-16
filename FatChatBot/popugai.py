import requests

def popugai():
    #url = 'https://images.app.goo.gl/TVy96u9r6aAGU3PU7'
    url = 'https://img.freepik.com/free-photo/closeup-of-a-scarlet-macaw-from-side-view-scarlet-macaw-closeup-head_488145-3540.jpg?size=626&ext=jpg'
    response = requests.get(url)
    if response.status_code:
        print(response)
        data = response.json()
        print(data)
        #return data.get('image')
