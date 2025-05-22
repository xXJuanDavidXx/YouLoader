# Descargar de YouTube

Herramienta sencilla para descargar audio y/o video desde YouTube.

## Requisitos

* Python 3.x
* Módulo `Descargar_video` (contiene la clase `Descargar_de_youtube`)
* `argparse` (incluido en la librería estándar)

## Uso

```bash
python nombre_del_script.py -l <LINK> [-r <RUTA>] (-v | -a)
```

### Parámetros

* `-l`, `--link`
  Link de YouTube a descargar. **Obligatorio**.
  Ejemplo: `https://www.youtube.com/watch?v=qMXESlny4-I`

* `-r`, `--ruta`
  Ruta local donde se guardará el archivo descargado.
  Si la ruta no existe, se preguntará si se desea crear.
  Si no se especifica, se descargará en el directorio actual.

* `-v`, `--video`
  Señala que se descargará el **video**.

* `-a`, `--audio`
  Señala que se descargará el **audio**.

> **Nota:** Debes elegir al menos una opción de descarga (`-v` y/o `-a`).

## Ejemplos

1. **Descargar solo el video** en el directorio actual:

   ```bash
   python descargar.py -l https://www.youtube.com/watch?v=qMXESlny4-I -v
   ```

2. **Descargar solo el audio** y guardarlo en `~/audios`:

   ```bash
   python descargar.py -l https://www.youtube.com/watch?v=qMXESlny4-I -r ~/audios -a
   ```

3. **Descargar audio y video** y guardarlos en `~/descargas`:

   ```bash
   python descargar.py -l https://www.youtube.com/watch?v=qMXESlny4-I -r ~/descargas -v -a
   ```

