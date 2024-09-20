import requests


def main():
    url = 'https://fakestoreapi.com/products'
    query_params = dict(limit=5)
    r = requests.get(url, params=query_params)

    if r.status_code != 200:
        print(r.text)
        exit(1)

    products = r.json()
    for p in products:
        print(f'{p['title']} --> {p['image']}')


if __name__ == '__main__':
    main()
    
# vinod@vinod.co
# 9731424784
