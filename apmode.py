import socket
import simpleaudio as sa
# use ifconfig -a to find this IP. If your pi is the first and only device connected to the ESP32, 
# this should be the correct IP by default on the raspberry pi
LOCAL_UDP_IP = "192.168.1.2"
SHARED_UDP_PORT = 4210
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
sock.bind((LOCAL_UDP_IP, SHARED_UDP_PORT))


def loop():
    current = ""
    first = 1
    while True:
        data, addr = sock.recvfrom(2048)
        print(data)
        values = str(data, 'ascii').strip()
        val_list = values.split(',')
        print(val_list)
        

        if val_list[1] == '1':
            lightVal = int(val_list[0])
            if lightVal >= 2048 and current != "waves.wav":
                print("waves")
                if first != 1:
                    if play_obj.is_playing():
                        play_obj.stop()
                wave_obj = sa.WaveObject.from_wave_file('waves.wav')
                play_obj = wave_obj.play()
                current = "waves.wav"
            elif lightVal < 2048 and current != "upbeatcrop.wav":
                print("upbeat")
                if first != 1:
                    if play_obj.is_playing() and first != 1:
                        play_obj.stop()
                wave_obj = sa.WaveObject.from_wave_file('upbeatcrop.wav')
                play_obj = wave_obj.play()
                current = "upbeatcrop.wav"
        else:
            play_obj.stop()
            first = 1
            current = ""
        
        first = 0
        
        
if __name__ == "__main__":
    loop()