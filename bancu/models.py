from django.db import models

# Usuário
class Usuario(models.Model):
    nome = models.CharField()
    endereco = models.CharField()
    cpf = models.IntegerField(primary_key=True)

# Conta Usuário

# Agência
class Agencia(models.Model):
    pass

# Tipo Conta
class TipoConta(models.Model):
    TIPO_CONTA = ((1,'Conta Poupança'),(2,'Conta Corrente'))

    tipo = models.CharField(max_length = 10, choices = TIPO_CONTA, blank = True)


# Conta Corrente e Poupança
class Corrente(models.Model):
    saldo = models.DecimalFields(decimal_places = 2)

# Cartão
class Cartao(models.Model):
    numero = models.IntegerField()
    conta = models.ForeignKey(ContaUsuario)
    validade = models.CharField()
    codigo_seg = models.IntegerField()
    nome_abv = models.CharField()

