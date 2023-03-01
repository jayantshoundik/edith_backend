from rest_framework.test import APIClient
import pytest
from apps.userpanel.models import *
client = APIClient()



@pytest.mark.django_db
def test_get_login():
    print("sdlkfskflkflksflk")
    payload = {
                "username": "username",
                "password":"Admin@123"
            }
    response = client.post('/api/v1/user/admin/login',payload)
    data = response.json()
    assert data['status'] == True


'''
Test case for Create master role 
'''
@pytest.mark.django_db
def test_create_role():
    payload = {
        "role": "OWNER",
        "is_active": True
    }
    response = client.post('/api/v1/user/user/create-role', payload, format='json')
    data = response.json()
    assert response.status_code == 201
    assert data['role']==payload['role']


@pytest.mark.django_db
def test_get_role_list():
    payload = {
        "role": "OWNER",
        "is_active": True
    }
    response2 = client.post('/api/v1/user/user/create-role', payload, format='json')
    response = client.get('/api/v1/user/user/create-role')
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_module_category():
    payload = {
        "name": "TestXtract",
        "is_active": True
    }
    response = client.post('/api/v1/user/admin/create-module-category', payload, format='json')
    print(response.data)
    data = response.json()
    assert response.status_code == 201
    assert data['name']==payload['name']

@pytest.mark.django_db
def test_create_module_category_list():
    payload = {
        "name": "TestXtract",
        "is_active": True
    }
    response1 = client.post('/api/v1/user/admin/create-module-category', payload, format='json')
    response = client.get('/api/v1/user/admin/create-module-category')
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 1    



@pytest.mark.django_db
def test_create_bazaar_app_category():
    payload = {
        "name": "TestXtract",
        "is_active": True
    }
    response = client.post('/api/v1/user/admin/create-bazaar-app-category', payload, format='json')
    data = response.json()
    assert response.status_code == 201
    assert data['name']==payload['name'] 


@pytest.mark.django_db
def test_create_bazaar_app_category_list():
    payload = {
        "name": "TestXtract",
        "is_active": True
    }
    response1 = client.post('/api/v1/user/admin/create-bazaar-app-category', payload, format='json')
    response = client.get('/api/v1/user/admin/create-bazaar-app-category')
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 1 


@pytest.mark.django_db
def test_create_module():
    payload = {
        "name": "TestXtract",
        "is_active": True
    }
    response = client.post('/api/v1/user/admin/create-module-category', payload, format='json')

    data = response.json()
    get_module_category = AppModuleCategory.objects.get(id=data['id'])
    payload_module = {
        "module": "XtractCheque",
        "title": "Extract Cheque",
        "description": "dsmdsnmsda ",
        "icon": None,
        "is_active": True,
        "category": get_module_category.id
    }
    response = client.post('/api/v1/user/admin/create-module', payload_module, format='json')

    data_2 = response.json()
    print("fdsfjkdsjfkjdskf...",data_2['module'])
    assert response.status_code == 201
    assert data_2['module'] == payload_module['module'] 

