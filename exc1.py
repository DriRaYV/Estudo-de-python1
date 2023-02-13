def retornaPercentualDeDesconto(fidelidade, compra, quantCompra):
    desconto = 0
    if fidelidade >= 10:
        desconto = 15
    if compra >= 1500:
        desconto += 17
    if quantCompra > 5:
        desconto += 13

    return desconto


def calculaCompra(valorCompra, valorDesconto):
    calculaValor = valorCompra - ((valorCompra * valorDesconto)/100)
    return calculaValor


print("O valor da compra com desconto foi de: " +
      calculaCompra(1000, retornaPercentualDeDesconto(11, 1600, 6)))
