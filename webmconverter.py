import subprocess

num = raw_input("Enter the number of webms you want to create: ")
vid = []
start = []
end = []
bitrate = []
width = []
height = []
out = []

for i in range(int(num)):
	vidin = raw_input("Enter the input file: ")
	vid.append(vidin)
	startin = raw_input("Enter the start time: ")
	start.append(startin)
	endin = raw_input("Enter the end time: ")
	end.append(endin)
	bitratein = raw_input("Enter the bitrate: ")
	bitrate.append(bitratein)
	widthin = raw_input("Enter the width: ")
	width.append(widthin)
	heightin = raw_input("Enter the  height: ")
	height.append(heightin)
	outin = raw_input("Enter the outpout file's name: ")
	out.append(outin)

for i in range(int(num)):
	subprocess.call('ffmpeg -i %s -ss %s -to %s -c:v libvpx -crf 4 -b:v %sK -vf scale=%s:%s %s.webm' % (vid[i], start[i], end[i], bitrate[i], width[i], height[i], out[i]), shell=True)