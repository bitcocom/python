import os
import subprocess

import pytube

yt = pytube.YouTube("https://www.youtube.com/watch?v=WH7xsW5Os10") #�ٿ���� ������ URL ����

vids= yt.streams.all()

#���� ���� ����Ʈ Ȯ��
for i in range(len(vids)):
    print(i,'. ',vids[i])

vnum = int(input("�ٿ� ���� ȭ����? "))

parent_dir = "C:\section2\download"
vids[vnum].download(parent_dir) #�ٿ�ε� ����

new_filename = input("��ȯ �� mp3 ���ϸ���?")

default_filename = vids[vnum].default_filename 
subprocess.call(['ffmpeg', '-i',                 #cmd ��ɾ� ����
    os.path.join(parent_dir, default_filename),
    os.path.join(parent_dir, new_filename)
])

print('������ �ٿ�ε� �� mp3 ��ȯ �Ϸ�!')
