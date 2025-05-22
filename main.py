##Autor: xXJuanDavidXx
##Github: https://github.com/xXJuanDavidXx

from Descargar_video import Descargar_de_youtube
import argparse
import sys
import os

def main(link, ruta, video, audio):
    """Main del programa, Revisa el link de youtube y ejecuta segun la condición"""
    
    ###Casos posibles###
    if link is None:
        print("[-] UnU Debes pasar un link de youtube")
        sys.exit()

    elif "youtube.com/watch?v" not in link:
        print("[-] UnU El link no es valido\n\n [+] OwO debes pasar un link de youtube valido, por ejemplo: https://www.youtube.com/watch?v=qMXESlny4-I")
        sys.exit()

    elif video is None or audio is None:
        print("[-] UnU Debes elegir al menos un tipo de descarga")
        sys.exit()

    elif ruta:
        if not os.path.exists(ruta):
            respuesta = input("[-] UnU La ruta ingresada no existe, deseas crearla? (s/n)")
            if respuesta.lower() == "s":
                os.makedirs(ruta)
            else:
                print("[-] x_x terminada la ejecucion, crea la ruta o usa una ruta existente")
                sys.exit()
        

    #Instancio el objeto para descargar.
    Descargar = Descargar_de_youtube()


    if video:
        Descargar.Descargar_video(link, ruta)

    elif audio:
        Descargar.Descargar_audio(link, ruta)

    elif audio and video:
        Descargar.Descargar_video(link, ruta)
        Descargar.Descargar_audio(link, ruta)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Herramienta sencilla para Descargar audio y video de youtube.")
    parser.add_argument("-l", "--link", type=str, help="Link de youtube")
    parser.add_argument("-r", "--ruta", type=str, help="Ruta de descarga")
    parser.add_argument("-v", "--video", action="store_true", help="Descargar video")
    parser.add_argument("-a", "--audio", action="store_true", help="Descargar audio")
    args = parser.parse_args()

    main(args.link, args.ruta, args.video, args.audio)
