from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

# Usuário
class Usuario(models.Model):
    nome = models.CharField()
    endereco = models.CharField()
    cpf = models.IntegerField(primary_key=True)

# Conta Usuário
class ContaUsuario(models.Model):
    numero_conta = models.IntegerField(primary_key=True)
    senha = models.IntegerField()
    corrente_ativa = models.BooleanField()
    poupanca_ativa = models.BooleanField()
    usuario=models.ForeignKey(Usuario)
# Agência
class Agencia(models.Model):
    contas = ArrayField(models.ForeignKey(ContaUsuario))

# Tipo Conta
TIPO_CONTA = ((1,'Conta Poupança'),(2,'Conta Corrente'))

class Contas(models.Model):
    saldo = models.FloatField()
    historico = JSONField()
    conta = models.ForeignKey(ContaUsuario)

class ContaCorrente(Contas):
    TIPO_CONTA = 2

class Poupanca(Contas):
    TIPO_CONTA = 1
    
class Cartao(models.Model):
    numero = models.IntegerField()
    conta = models.ForeignKey(ContaUsuario)
    validade = models.CharField()
    codigo_seg = models.IntegerField()
    nome_abv = models.CharField()

