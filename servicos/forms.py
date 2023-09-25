from django.forms import ModelForm
from .models import Servico, CategoriaManutencao

class FormServico(ModelForm):
    class Meta:
        model = Servico
        exclude = ['finalizado', 'protocole']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            print(field)
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder': field})
            

        choices = list()
        for i, j in self.fields['categoria_manutencao'].choices:
            categoria = CategoriaManutencao.objects.get(titulo=j)
            choices.append((i.value, categoria.get_titulo_display()))
        

        print(choices)
        self.fields['categoria_manutencao'].choices = choices