import os
import sys
import subprocess

class semi():
	def exercici1(self):	
		print("Diga'm a quina resolució vols canviar el vídeo")
		print("Opció 1: 720p")
		print("Opció 2: 480p")
		print("Opció 3: 360x240")
		print("Opció 4: 160x120")
		n = input()
		if(n=="1"):
			subprocess.call(['ffmpeg', '-i', 'tall.mp4', "-filter:v", "scale=1280:720", '-c:a', 'copy', 'resolucio.mp4'])
		elif(n=="2"):
			subprocess.call(['ffmpeg', '-i', 'tall.mp4', "-filter:v", "scale=640:480", '-c:a', 'copy', 'resolucio.mp4'])
		elif(n=="3"):
			subprocess.call(['ffmpeg', '-i', 'tall.mp4', "-filter:v", "scale=360:240", '-c:a', 'copy', 'resolucio.mp4'])
		elif(n=="4"):
			subprocess.call(['ffmpeg', '-i', 'tall.mp4', "-filter:v", "scale=160:1200", '-c:a', 'copy', 'resolucio.mp4'])
		else:
			print("opció incorrecta")
		'''
		'''
		print("Diga'm quin tipus de vídeo codec vols")
		print("Opció 1: VP8")
		print("Opció 2: VP9")
		print("Opció 3: h265")
		print("Opció 4: AV1")
		n = input()
		if n == '1':
			subprocess.call(['ffmpeg', '-i', 'resolucio.mp4', "-c:v", 'libvpx', "-b:v", '1M', "-c:a", 'libvorbis', 'vp8.webm'])
		elif n == '2':
			subprocess.call(['ffmpeg', '-i', 'resolucio.mp4', "-c:v", "libvpx-vp9", "-b:v", '1M', "-c:a", 'libvorbis', 'vp9.webm'])
		elif n == '3':
			    subprocess.call(['ffmpeg', '-i', 'resolucio.mp4', "-c:v", 'libx265', '-crf', '26', '-preset', 'fast', "-c:a", 'aac', "-b:a", '128k', 'h265.mp4'])
		elif n == '4':
			    subprocess.call(['ffmpeg', '-i', 'resolucio.mp4', '-strict', '-2' "-c:v", "libaom-av1", '-crf', '30', "-b:v", '0', "av1.mp4"])

	def exercici2(self):			
		subprocess.call(['ffmpeg', '-i', 'vp8.webm', '-i', 'h265.mp4', "-filter_complex", 'hstack', 'comparacio.webm'])
		print("Comparem vp8 a l'esquerra i h265 a la dreta")
		print("Trobo que són similars però podem veure diferències subtils")
		print("vp8 es codifica més ràpid")
		print("vp8 es codifica més ràpid")
	def exercici3(self):
		subprocess.call(['ffmpeg', '-i',  'resolucio.mp4',  '-f',  'mpegts', 'udp://@127.0.0.1:23000'])
		print("s'ha d'obrir una altra terminal i posar la següent ordre")
		print("ffplay udp://127.0.0.1:23000")
		
	def exercici4(self):
		print("escrip l'IP on vols fer el prodcast del video")
		ip = input()
		stream = 'udp://'+ip+':23000'
		subprocess.call(['ffmpeg', '-i',  'resolucio.mp4',  '-f',  'mpegts', stream])
		print("s'ha d'obrir una altra terminal i posar la següent ordre")
		print("ffplay udp://IP:23000")

