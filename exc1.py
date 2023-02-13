def retornaPercentualDesconto(fidelidade, copmra, quantCompra):
    desconto = 0
    if fidelidade >= 10:
        desconto = 15
    if copmra >= 1500:
        desconto += 17
    if quantCompra > 5:
        desconto += 13

    return desconto


def calculaCompra(valorCompra, valorDesconto):
    calculaValor = valorCompra - ((valorCompra * valorDesconto)/100)
    return calculaValor


print(calculaCompra(1000, retornaPercentualDesconto(11, 1600, 6)))
