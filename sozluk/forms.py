from django import forms
from sozluk.models import Entry, Post


class EntryForm(forms.Form):
    title = forms.CharField(required=True, label="başlık")
    body = forms.CharField(required=True, label="entry")

    def clean_title(self):
        title = self.cleaned_data.get('title').strip()
        if len(title) > 120:
            raise forms.ValidationError("120 karakterden kısa,5 karakterden \
                                        uzun başlık gir")
        return title

    def clean_body(self):
        body = self.cleaned_data.get('body').strip()
        if len(body) < 10:
            raise forms.ValidationError("hacı hiç bi şey yazmadın ki")
        return body


class PostForm(forms.Form):
    body = forms.CharField(required=True)

    def clean_body(self):
        body = self.cleaned_data.get('body').strip()
        if len(body) < 5:
            raise forms.ValidationError("daha uzun bi şey yazsan")
        return body
