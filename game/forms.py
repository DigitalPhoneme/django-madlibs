from django import forms

class MadLibsForm(forms.Form):
    def __init__(self, prompts, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for prompt in prompts:
            self.fields[prompt] = forms.CharField(
                label=prompt.replace('_', ' ').title(),
                widget=forms.TextInput(attrs={'class': 'form-control'}),
                required=False,
                min_length=3,
            )