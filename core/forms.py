from django import forms
from .models import Mensaje


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ["nombre", "email", "asunto", "contenido"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "campo"}),
            "email": forms.EmailInput(attrs={"class": "campo"}),
            "asunto": forms.TextInput(attrs={"class": "campo"}),
            "contenido": forms.Textarea(attrs={"class": "campo", "rows": 5}),
        }

    # Validaciones que se ejecutan en el SERVIDOR al llamar a is_valid():
    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"].strip()
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre

    def clean_contenido(self):
        contenido = self.cleaned_data["contenido"].strip()
        if len(contenido) < 10:
            raise forms.ValidationError("El mensaje es demasiado corto (mínimo 10 caracteres).")
        return contenido

    def clean(self):
        cleaned = super().clean()
        asunto = cleaned.get("asunto", "")
        contenido = cleaned.get("contenido", "")
        if asunto and contenido and asunto.strip() == contenido.strip():
            self.add_error("asunto", "El asunto no puede ser igual al contenido.")
        return cleaned