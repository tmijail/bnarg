# -*- coding: utf-8 -*-


"""bnarg.bnarg: provides entry point main()."""


__version__ = "0.1.0"


import requests
import bs4
import click


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--moneda', '-m', default='Dolar U.S.A', help='Moneda a consultar. [default: Dolar U.S.A]')
@click.option('--billetes/--divisas', '-b/-d', default=True, help='Tipo de cotización. [default: --billetes]')
def main(moneda, billetes):
    """
    Busca la cotización actual de la moneda seleccionada según el Banco Nación.\n
    Las devuelve en el siguiente formato\n
        [Fecha] [Valor de compra] [Valor de venta]\n
    Por ejemplo,\n
        18/2/2020 58,2500 63,2500
    """
    try:
        if billetes:
            cotiz = cotizacion(moneda, 'billetes')
        else:
            cotiz = cotizacion(moneda, 'divisas')
    except:
        print("\033[1;31mERROR:\033[0m", "No se ha podido obtener la cotización.")
        return -1

    print(cotiz['fecha'], cotiz['compra'], cotiz['venta'])
    return 0


def cotizacion(moneda='Dolar U.S.A', tipo='billetes'):
    soup = bs4.BeautifulSoup(
        requests.get('https://www.bna.com.ar/Personas').content,
        'html.parser')
    tabla = soup.find(id=tipo)
    cotiz = tabla.find(string=moneda).parent.parent.find_all('td')

    fecha = str(tabla.thead.find(class_='fechaCot').string)
    compra = cotiz[1].string
    venta = cotiz[2].string

    return dict(fecha=fecha, compra=compra, venta=venta, tipo=tipo, moneda=moneda)
