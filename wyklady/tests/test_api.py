import pytest
from wyklady.szkolenia.models import *


def test__add_uczestnik(authorized_client):
    data_to_save = {
        'imie': 'testowy',
        'nazwisko': 'uczestnik',
        'email': 'email',
        'telefon': '795937248'
    }

    url = 'http://127.0.0.1:8000/api/uczestnicy'

    response = authorized_client.post(
        url,
        data_to_save,
        content_type='application/json',
    )
    assert response.status_code == 200
    assert response.json() == data_to_save
    all_uczestnicy = Uczestnicy.objects.all()
    assert all_uczestnicy.count() == 1

    saved_animal = all_uczestnicy.first()
    assert saved_animal.imie == 'testowy'
    assert saved_animal.nazwisko == 'uczestnik'
    assert saved_animal.email == 'email'
    assert saved_animal.telefon == '795937248'
