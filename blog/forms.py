from django import forms


class MessageForm(forms.Form):
    """
    Form for new blog record.
    """

    title = forms.CharField(
        max_length=100,
        label='Заголовок сообщения.',
        error_messages={'required': 'Вы должны ввести заголовок сообщения.'}
    )
    text = forms.CharField(
        max_length=1000,
        label='Текст сообщения.',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 30}),
        error_messages={'required': 'Вы должны ввести текст сообщения.'}
    )
