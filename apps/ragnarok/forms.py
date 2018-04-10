import hashlib

from django import forms

from apps.players.models import Player

from .models import Account


class AccountCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ['username', 'email']
        widgets = {'username': forms.HiddenInput(), 'email': forms.HiddenInput()}

    def clean(self):
        cleaned_data = super(AccountCreationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error('confirm_password', 'The passwords do not match.')

        return cleaned_data

    def save(self):
        data = self.cleaned_data
        account, created = Account.objects.get_or_create(
            username=data['username'],
            password=hashlib.md5(data['password'].encode('utf-8')).hexdigest(),
        )

        if created:
            account.save()

            # Save the `account_id` to the player's user account.
            player = Player.objects.get(username=data['username'])
            player.account_ids = [account.pk]
            player.save()

        return account
