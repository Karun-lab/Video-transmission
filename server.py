import socket
import cv2
import pickle
import struct
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
print("host name", host_name)
host_ip = socket.gethostbyname(host_name)
print('HOST IP:', host_ip)
port = 8989
socket_address = (host_ip, port)
server_socket.bind(socket_address)
server_socket.listen(5)
print("LISTENING AT:", socket_address)

while True:
    client_socket, addr = server_socket.accept()
    print('GOT CONNECTION FROM:', addr)
    if client_socket:
        vid = cv2.VideoCapture(0)

        while(vid.isOpened()):
            img, frame = vid.read()
            gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
            for (x, y, w, h) in faces:
                print(x,y,w,h)
                roi_gray = gray[y:y+h, x:x+w] #(ycord_start, ycord_end)
                roi_color = frame[y:y+h, x:x+w]
                color = (255, 0, 0) #BGR 0-255 
                stroke = 2
                end_cord_x = x + w
                end_cord_y = y + h
                cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a)) + a
            client_socket.sendall(message)

            #cv2.imshow('TRANSMITTING VIDEO', frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                client_socket.close()