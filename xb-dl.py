import argparse
import series_parser
import ep_downloader
import os

base_url="https://xabarin.gal/"
video_endpoint = "videos/"
details_endpoint = "videos/detail/"

def main():
    parser = argparse.ArgumentParser(
        prog="XB-DL",
        description="Script de descarga secuencial de episodios das series de xabarin.gal baseado en yt-dlp"
    )
    parser.add_argument("url", type=str, help="URL da serie a descargar")
    parser.add_argument("-o", "--outputdir", type=str, help="Directorio de saída para almacenar os episodios descargados da serie")
    parser.add_argument("-f", "--forceredownload", action='store_true', help="Forza a re-descarga dos episodios que xa existan no directorio" )

    args = parser.parse_args()

    info = series_parser.get_series_info(args.url)
    urls = series_parser.get_series_episodes(args.url)

    for ep_url in urls:
        ep_data = series_parser.get_episode_details(f"{base_url}{details_endpoint}{ep_url}")
        video_m3u8 = series_parser.get_episode_m3u8(f"{base_url}{video_endpoint}{ep_url}")

        outdir = "."
        if args.outputdir != None:
            outdir = args.outputdir
        if os.path.isdir(outdir):
            ep_downloader.download_m3u8(video_m3u8, info, ep_data, output_dir=outdir, overwrites=args.forceredownload)
        else:
            print(f"{outdir} non existe no sistema, abortando")
            break
        
if __name__ == "__main__":
    main()