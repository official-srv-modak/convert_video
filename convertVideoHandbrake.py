import os, sys

def convert(resolution, input_file_name, output_file_name):
    command = "HandBrakeCLI -i \""+input_file_name+"\" -o \""+output_file_name+"\" -Z \"Very Fast 720p30\""
    #command = "ffmpeg.exe -y -i \""+input_file_name+"\" -vf scale="+resolution+":-2,setsar=1:1 -c:v libx264 -c:a copy \""+output_file_name+"\" -preset ultrafast -bufsize 8000k"
    print(command)
    os.system(command)


def get_output_path(file_path, resolution):
    #file_path = file_path.split(os.sep)[-1]
    split_list = file_path.split(".")
    output_path = ""
    for val in range(0, len(split_list) - 1):
        output_path += split_list[val] + "."
    output_path += "x" + resolution
    output_path += "."+split_list[-1]
    return output_path

def start_process():

    if len(sys.argv) > 1:
        file_path = sys.argv[1];
        resolution = sys.argv[2];
        output_path = get_output_path(file_path, resolution)
        convert(resolution, file_path, output_path)
    else:
        file_path = input("Input file path\n")
        resolution = input("Input target resolution\n")
        output_path = get_output_path(file_path, resolution)
        convert(resolution, file_path, output_path)

start_process()