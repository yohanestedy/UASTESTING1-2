import json

from .settings import DEFAULT_PRICE

def test_product_detail_api(client):
    id = 3
    response = client.get(f"/api/products/{id}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert id == data.get('id')
    assert DEFAULT_PRICE * id


def test_product_api(client):
    response = client.get("/api/products")
    assert response.status_code == 200

# post new cart
def test_post_cart(client):
    product_data = {
        'sku': 'SKU123',
        'brand': 'BrandXYZ',
        'name': 'ProductXYZ',
        'description': 'DescriptionXYZ',
        'price': 10.99,
        'non_discountable': True,
    }

    response = client.post('/api/products', json=product_data)
    assert response.status_code == 200

    assert response.get_data(as_text=True) == 'Data berhasil ditambahkan'
