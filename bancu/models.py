from django.db import models

# Usuário

# Conta Usuário

# Agência

# Tipo Conta
class TipoConta(models.Model):
    TIPO_CONTA = ((1,'Conta Poupança'),(2,'Conta Corrente'))

    tipo = models.CharField(max_lenght = 10, choices = TIPO_CONTA, blank = True)



# Conta Corrente e Poupança

# Cartão


