import json
import requests

if __name__ == '__main__':
    email = input("Inserisci la tua mail: ")
    password = input("Inserisci la tua password: ")


    loginreq = requests.post('https://joblabsmarteducation.idea360.com/api/accounting/access/login', json={'Email': email, 'Password': password})

    print(loginreq.text)


    if not loginreq.json()['Success']:
        exit(1)

    authtoken = loginreq.json()['Token']
    heardersreq = {"Authorization": authtoken}


    richiestalezioni = requests.post('https://joblabsmarteducation.idea360.com/api/courses/main/get/414/lessons', headers=heardersreq)

    input('sicuro? ')

    for item in richiestalezioni.json()['lessons']['units'][0]['modules']:
        idlezione = str(item['item']['id'])

        avviolezreq = requests.post('https://joblabsmarteducation.idea360.com/api/courses/sessions/start/414/' + idlezione, headers=heardersreq)

        idsessione = str(avviolezreq.json()['sessionId'])

        richiestacomplet = requests.post(
            'https://joblabsmarteducation.idea360.com/api/courses/sessions/set-completed/' + idsessione, headers=heardersreq)

        print(richiestacomplet.text)

    print('fatto fratelo')