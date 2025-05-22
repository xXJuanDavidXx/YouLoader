import yt_dlp
import os


class Descargar_de_youtube:
    def __init__(self):
        self.videos = "Descargas_Videos"
        self.audios = "Descargas_Audios"



    def Descargar_video(self, link, ruta=None):
        """
        Descarga video de youtube
        """

        if ruta == None:
            ruta = self.videos

        opciones = {
                'format':'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
                'outtmpl': os.path.join(ruta, '%(title)s.%(ext)s'), #Guarda el archivo en la ruta especificada
                'quiet': True,
                'no_warnings': True,
                'merge_output_format': 'mp4'
                } #Opciones de descarga
        try:
            print(f"[+] Uw7 Descargando video...\n")
            with yt_dlp.YoutubeDL(opciones) as ydl: #Descarga el video.
                ydl.download([link])
                info = ydl.extract_info(link, download=False)
                ruta_des = ydl.prepare_filename(info)
                print("[+] UwU El video se descargo correctamente en la ruta: ", ruta_des)


        except Exception as e:
            print(e)


    def Descargar_audio(self, link, ruta=None):
        """
        Descarga audio de youtube
        """

        if ruta == None:
            ruta = self.audios

        opciones = {
                'format':'bestaudio[ext=m4a]/mp4',
                'outtmpl': os.path.join(ruta, '%(title)s.%(ext)s'), #Guarda el archivo en la ruta especificada
                'quiet': True,
                'no_warnings': True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                } #Opciones de descarga
        

        try:
            print("[+] Uw7 Descargando audio...\n")
            with yt_dlp.YoutubeDL(opciones) as ydl: #Descarga el video.
                ydl.download([link])
                info = ydl.extract_info(link, download=False)
                ruta_des = ydl.prepare_filename(info)
                print("[+] UwU El video se descargo correctamente en la ruta: ", ruta_des)

        except Exception as e:
            print(e)



#link = "https://www.youtube.com/watch?v=wWoQ7PFSYlk"

#Descargar_video(link)
