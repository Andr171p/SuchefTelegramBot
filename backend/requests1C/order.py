import requests

from misc.utils import format_phone_number


# return only one client orders from phone number:
def get_order_response(client_phone_number):
    formated_phone_number = format_phone_number(client_phone_number)

    url = 'https://noname-sushi.online/web/hs/hook?token=NTAxNGVhNWMtZTUwYi00NTdjLTk5NTctNmIyMmM2N2U5NzRh'

    headers = {
        'Content-Type': 'application/json; charset=UTF-8'
    }

    data = {
        'command': 'status',
        'telefon': f'{formated_phone_number}'
    }

    response = requests.post(url, headers=headers, json=data)

    return response.json()


# return all today orders at the moment:
def get_all_orders_response():
    url = 'https://noname-sushi.online/web/hs/hook?token=NTAxNGVhNWMtZTUwYi00NTdjLTk5NTctNmIyMmM2N2U5NzRh'

    headers = {
        'Content-Type': 'application/json; charset=UTF-8'
    }

    data = {
        'command': 'statuses',
        'active': 'true'
    }
    try:
        response = requests.post(url, headers=headers, json=data)

        return response.json()
    except Exception as _ex:
        print(f"ERROR from server: {response.content}\n"
              f"{_ex}")
        return -1


print(get_all_orders_response())