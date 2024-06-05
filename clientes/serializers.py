from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_cpf(self, cpf):
        if len (cpf) != 11:
            raise serializers.ValidationError(" O CPF tem que ter 11 digitos")
        return cpf

    def validate_nome(self, nome):
        if nome.isalpha():
            raise serializers.ValidationError('Não é permitido numéro')
        return nome

    def validate_rg(self, rg):
        if len(rg) != 9:
            raise serializers.ValidationError(" O RG não pode ter meno de 9 digitos")
        return rg
    def validate_celular(self, celular):
        if len(celular) < 11:
            raise serializers.ValidationError(" O celular tem que ter 11 digitos")
        return celular


    