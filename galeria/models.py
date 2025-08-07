from django.db import models

OPCOES_CATEGORIA = [
    ('NEBULOSA', 'Nebulosa'),
    ('GALAXIA', 'Galáxia'),
    ('ESTRELA', 'Estrela'),
    ('PLANETA', 'Planeta'),
]

class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, null=False, default='')
    foto = models.CharField(max_length=150, null=False, blank=False)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"