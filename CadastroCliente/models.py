from django.db import models

# Create your models here.
class Profissao(models.Model):
    nome = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "profissões"

class Interesse (models.Model):
    nome = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome



class Cliente(models.Model):
    ESTADO_CIVIL = [
        ('SOL', 'Solteiro'),
        ('CAS', 'Casado'),
        ('DIV', 'Divorciado'),
        ('VIU', 'Viuvo')
    ]
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14, unique=True)

    data_nascimento = models.DateField()
    email = models.EmailField(max_length=100, unique=True)
    endereco = models.CharField(max_length=250, null=True, verbose_name= "Endereço")
    nro = models.IntegerField(null=True)
    bairro = models.CharField(max_length=50, null=True)
    cidade = models.CharField(max_length=50, null=True)
    cep = models.CharField(max_length=9, null=True)
    matricula = models.IntegerField(unique=True, verbose_name= "Matrícula")
    renda_mensal = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(verbose_name="Usuário ativo? ")
    estado_civil = models.CharField(max_length=3, choices=ESTADO_CIVIL, null=True)
    profissao = models.ForeignKey(Profissao, on_delete=models.SET_NULL, null=True)
    interesses = models.ManyToManyField(Interesse)

    def __str__(self):
        return self.nome
    
class Telefone(models.Model):
    ddd = models.CharField(max_length=2)
    numero = models.CharField(max_length=10)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.ddd}) {self.numero}"