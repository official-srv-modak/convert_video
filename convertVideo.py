import os, sys
from pathlib import Path

def convert(input_file_name, output_file_name):
    """command = ./ffmpeg -hide_banner -y -i \""""+input_file_name+"""\"\\
  -vf scale=w=640:h=360:force_original_aspect_ratio=decrease -c:a aac -ar 48000 -c:v h264 -profile:v main -crf 20 -sc_threshold 0 -g 48 -keyint_min 48 -hls_time 4 -hls_playlist_type vod  -b:v 800k -maxrate 856k -bufsize 1200k -b:a 96k -hls_segment_filename """+output_file_name+"""/360p_%03d.ts """+output_file_name+"""/360p.m3u8 \
  -vf scale=w=842:h=480:force_original_aspect_ratio=decrease -c:a aac -ar 48000 -c:v h264 -profile:v main -crf 20 -sc_threshold 0 -g 48 -keyint_min 48 -hls_time 4 -hls_playlist_type vod -b:v 1400k -maxrate 1498k -bufsize 2100k -b:a 128k -hls_segment_filename """+output_file_name+"""/480p_%03d.ts """+output_file_name+"""/480p.m3u8 \
  -vf scale=w=1280:h=720:force_original_aspect_ratio=decrease -c:a aac -ar 48000 -c:v h264 -profile:v main -crf 20 -sc_threshold 0 -g 48 -keyint_min 48 -hls_time 4 -hls_playlist_type vod -b:v 2800k -maxrate 2996k -bufsize 4200k -b:a 128k -hls_segment_filename """+output_file_name+"""/720p_%03d.ts """+output_file_name+"""/720p.m3u8 \
  -vf scale=w=1920:h=1080:force_original_aspect_ratio=decrease -c:a aac -ar 48000 -c:v h264 -profile:v main -crf 20 -sc_threshold 0 -g 48 -keyint_min 48 -hls_time 4 -hls_playlist_type vod -b:v 5000k -maxrate 5350k -bufsize 7500k -b:a 192k -hls_segment_filename """+output_file_name+"""/1080p_%03d.ts """+output_file_name+"""/1080p.m3u8
"""
    nameWithoutExtension = output_file_name.split(".m3u8")[0]
    path = Path(input_file_name)
    parentDir = str(path.parent.absolute())
    justName = nameWithoutExtension.split(os.sep)[-1]
    print(parentDir)

    if(os.sep == "\\"):
        command = """ffmpeg -hide_banner -y -i """+input_file_name+""" \\
  -crf 20 -sc_threshold 0 -g 48 -keyint_min 48 -ar 48000 \\
  -map 0:v:0 -map 0:v:0 -map 0:v:0 -map 0:a:0 -map 0:a:0 -map 0:a:0 \\
  -c:v:0 h264 -profile:v:0 main -filter:v:0 "scale=w=640:h=360:force_original_aspect_ratio=decrease" -b:v:0 800k -maxrate:v:0 856k -bufsize:v:0 1200k \\
  -c:v:1 h264 -profile:v:1 main -filter:v:1 "scale=w=842:h=480:force_original_aspect_ratio=decrease" -b:v:1 1400k -maxrate:v:1 1498k -bufsize:v:1 2100k \\
  -c:v:2 h264 -profile:v:2 main -filter:v:2 "scale=w=1280:h=720:force_original_aspect_ratio=decrease" -b:v:2 2800k -maxrate:v:2 2996k -bufsize:v:2 4200k \\
  -c:a:0 aac -b:a:0 96k \\
  -c:a:1 aac -b:a:1 128k \\
  -c:a:2 aac -b:a:2 128k \\
  -var_stream_map "v:0,a:0 v:1,a:1 v:2,a:2" \\
  -master_pl_name testvideo.m3u8 \\
  -f hls -hls_time 4 -hls_playlist_type vod -hls_list_size 0 \\
  -hls_segment_filename '"""+parentDir+os.sep+justName+os.sep+justName+"-v%v"+os.sep+justName+"""%03d.ts' """+parentDir+os.sep+justName+os.sep+justName+"-v%v"+os.sep+justName+""".m3u8"""

    else:
        command = """./ffmpeg -hide_banner -y -i """+input_file_name+""" \\
  -crf 20 -sc_threshold 0 -g 48 -keyint_min 48 -ar 48000 \\
  -map 0:v:0 -map 0:v:0 -map 0:v:0 -map 0:a:0 -map 0:a:0 -map 0:a:0 \\
  -c:v:0 h264 -profile:v:0 main -filter:v:0 "scale=w=640:h=360:force_original_aspect_ratio=decrease" -b:v:0 800k -maxrate:v:0 856k -bufsize:v:0 1200k \\
  -c:v:1 h264 -profile:v:1 main -filter:v:1 "scale=w=842:h=480:force_original_aspect_ratio=decrease" -b:v:1 1400k -maxrate:v:1 1498k -bufsize:v:1 2100k \\
  -c:v:2 h264 -profile:v:2 main -filter:v:2 "scale=w=1280:h=720:force_original_aspect_ratio=decrease" -b:v:2 2800k -maxrate:v:2 2996k -bufsize:v:2 4200k \\
  -c:a:0 aac -b:a:0 96k \\
  -c:a:1 aac -b:a:1 128k \\
  -c:a:2 aac -b:a:2 128k \\
  -var_stream_map "v:0,a:0 v:1,a:1 v:2,a:2" \\
  -master_pl_name testvideo.m3u8 \\
  -f hls -hls_time 4 -hls_playlist_type vod -hls_list_size 0 \\
  -hls_segment_filename '"""+parentDir+os.sep+justName+os.sep+justName+"-v%v"+os.sep+justName+"""%03d.ts' """+parentDir+os.sep+justName+os.sep+justName+"-v%v"+os.sep+justName+""".m3u8"""

    

    #command = "./ffmpeg -i \""+input_file_name+"\" -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k \-movflags +faststart -vf scale=-2:720,format=yuv420p \""+output_file_name+"\""
    #command = "./HandBrakeCLI -i \""+input_file_name+"\" -o \""+output_file_name+"\" -Z \"Very Fast 720p30\""
    #command = "./ffmpeg -i \""+input_file_name+"\" -profile:v baseline -level 3.0 -s 640x360 -start_number 0 -hls_time 10 -hls_list_size 0 -f hls \""+output_file_name+"\""
    #command = "ffmpeg.exe -y -i \""+input_file_name+"\" -vf scale="+resolution+":-2,setsar=1:1 -c:v libx264 -c:a copy \""+output_file_name+"\" -preset ultrafast -bufsize 8000k"
    
    print(command)

    #command = ""
    os.system(command)


def get_output_path(file_path):
    #file_path = file_path.split(os.sep)[-1]
    split_list = file_path.split(".")
    output_path = ""
    for val in range(0, len(split_list) - 1):
        output_path += split_list[val] + "."
    #output_path += "x" + resolution
    output_path += "m3u8"
    return output_path

def start_process():

    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        output_path = get_output_path(file_path)
        #output_path = "video.m3u8"
        convert(file_path, output_path)
    else:
        file_path = input("Input file path\n")
        output_path = get_output_path(file_path)
        #output_path = "video.m3u8"
        convert(file_path, output_path)

start_process()
