from django import forms


class MessageForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        label='Заголовок сообщения.',
        error_messages={'required': 'Вы должны ввести заголовок сообщения.'}
    )
    text = forms.CharField(
        max_length=1000,
        label='Текст сообщения.',
        error_messages={'required': 'Вы должны ввести текст сообщения.'}
    )
