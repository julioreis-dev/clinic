import pytest


pytestmark = pytest.mark.django_db

def test_create_user(customuser):
    user = customuser.objects.create(username='will', email='will@email.com', password='testpass123')
    assert user.username == 'will'
    assert user.email == 'will@email.com'
    assert user.password == 'testpass123'
    assert user.is_active
    assert user.is_staff == False
    assert user.is_superuser == False
    assert customuser.objects.all().count() == 1