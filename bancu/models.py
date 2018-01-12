from django.db import models

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
    pass
# Tipo Conta

# Conta Corrente e Poupança

# Cartão
class Cartao(models.Model):
    numero = models.IntegerField()
    conta = models.ForeignKey(ContaUsuario)
    validade = models.CharField()
    codigo_seg = models.IntegerField()
    nome_abv = models.CharField()

