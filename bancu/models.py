from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

# Usuário
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cpf = models.IntegerField(primary_key=True)

# Conta Usuário
class ContaUsuario(models.Model):
    numero_conta = models.IntegerField(primary_key=True)
    senha = models.IntegerField()
    corrente_ativa = models.BooleanField()
    poupanca_ativa = models.BooleanField()
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
# Agência
class Agencia(models.Model):
    contas = models.ManyToManyField(ContaUsuario)

# Tipo Conta
TIPO_CONTA = ((1,'Conta Poupança'),(2,'Conta Corrente'))

class Contas(models.Model):
    saldo = models.FloatField()
    historico = JSONField()
    conta = models.ForeignKey(ContaUsuario, on_delete=models.CASCADE)

class ContaCorrente(Contas):
    TIPO_CONTA = 2

class Poupanca(Contas):
    TIPO_CONTA = 1

class Cartao(models.Model):
    numero = models.IntegerField()
    conta = models.ForeignKey(ContaUsuario, on_delete=models.CASCADE)
    validade = models.CharField(max_length=10)
    codigo_seg = models.IntegerField()
    nome_abv = models.CharField(max_length=50)

