function main(args)
lat = subwrd(args,1)
lon = subwrd(args,2)

* Especificar o arquivo a ser aberto
'sdfopen example.nc'

'set lat 'lat
'set lon 'lon

* Eventualmente trocar o time
ti=1
'set t 'ti

* Alterar nome da variável
'd CPD'
res=result
var=subwrd(res,4)

* Imprime resultado na tela
say var

'quit'
