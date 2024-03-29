# xb-dl

xb-dl é un descargador de series de xabarin.gal que usa yt-dlp para baixar os arquivos incrustados nos streams da web

## Instalación
``pip install -r requirements.txt``

## Uso
``python xb-dl.py url_da_serie``

```
usage: XB-DL [-h] [-o OUTPUTDIR] [-f] url

Script de descarga secuencial de episodios das series de xabarin.gal baseado en yt-dlp

positional arguments:
  url                   URL da serie a descargar

options:
  -h, --help            show this help message and exit
  -o OUTPUTDIR, --outputdir OUTPUTDIR
                        Directorio de saída para almacenar os episodios descargados da serie
  -f, --forceredownload
                        Forza a re-descarga dos episodios que xa existan no directorio
```

## Vantaxes
- Non se re-descargan episodios, co cal é seguro chamar ó script varias veces (dende un servidor, por exemplo) para ir tendo sempre unha serie actualizada
- Se se interrompe unha descarga, retómase simplemente chamando de novo ó script

## Limitacións

O software está aínda en desenvolvemento temprano e está relativamente limitado, principalmente por:
- Só descarga unha temporada de cada serie (a que saia ó cargar a páxina da serie)
- Só descarga a mellor calidade dispoñible dos capítulos
- A descarga é secuencial

## Traballo futuro
Podes colaborar co proxecto facendo un fork e pull request cas features que desexes, por agora as seguintes cousas a desenvolver son:
- Descarga de Multi-Temporada
- Descarga de capítulos ou rangos de capítulos específicos
- Descarga en paralelo de varios capítulos
- Selección de calidade a descargar