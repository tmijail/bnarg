bnarg
========================

Paquete no oficial que permite obtener las cotizaciones actuales que se ven en la
[página principal del BNA](https://www.bna.com.ar/Personas).

Uso
-----

El paquete puede importarse desde un script de python

```python
>>> import bnarg as bna
>>> bna.cotizacion(moneda='Dolar U.S.A', tipo='billetes')
{'fecha': '18/2/2020', 'compra': '58,2500', 'venta': '63,2500', 'tipo': 'billetes', 'moneda': 'Dolar U.S.A'}
```

O como un programa de consola

```bash
$ bnarg -m "Dolar U.S.A" --billetes
18/2/2020 58,2500 63,2500
```

Para obtener ayuda acerca de las opciones disponibles se puede ejecutar `bnarg --help`.

Instalación
-----
Para instalarlo hay que clonar el repositorio y ejecutar `setup.py`
```bash
$ git clone https://github.com/tmijail/bnarg.git
$ cd bnarg
$ python setup.py install
```
