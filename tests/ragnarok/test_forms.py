import hashlib
import pytest

from apps.players.factories import PlayerFactory
from apps.players.models import Player
from apps.ragnarok.forms import AccountCreationForm


@pytest.mark.parametrize(
    'password, confirm_password, validity',
    [('testpass', 'testpass', True), ('testpass', 't3stpass', False)],
)
def test_account_form(password, confirm_password, validity):
    form = AccountCreationForm(
        data={
            'username': 'bryan',
            'email': 'bryan@avalonstar.tv',
            'password': password,
            'confirm_password': confirm_password,
        }
    )

    assert form.is_valid() is validity


@pytest.mark.django_db
def test_account_creation():
    factory = PlayerFactory(username='bryan')
    form = AccountCreationForm(
        data={
            'username': 'bryan',
            'email': 'bryan@avalonstar.tv',
            'password': 'testpass',
            'confirm_password': 'testpass',
        }
    )

    if form.is_valid():
        account = form.save()
        assert account.username == 'bryan'
        assert account.password == hashlib.md5('testpass'.encode('utf-8')).hexdigest()

        player = Player.objects.get(username='bryan')
        assert player.account_ids == [account.pk]
