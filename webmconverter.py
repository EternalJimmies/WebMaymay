import subprocess
vid = raw_input("Enter the input file: ")
start = raw_input("Enter the start time: ")
end = raw_input("Enter the end time: ")
bitrate = raw_input("Enter the bitrate: ")
width = raw_input("Enter the width: ")
height = raw_input("Enter the  height: ")
out = raw_input("Enter the outpout file's name: ")
subprocess.call('ffmpeg -i %s -ss %s -to %s -c:v libvpx -crf 4 -b:v %sK -vf scale=%s:%s %s.webm' % (vid, start, end, bitrate, width, height, out), shell=True)