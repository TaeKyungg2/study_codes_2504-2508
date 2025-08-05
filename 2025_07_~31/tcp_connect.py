# server.py
import socket

HOST = '0.0.0.0'
PORT = 10000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"서버 실행 중: {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"클라이언트 접속: {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"받은 데이터: {data.decode()}")
            conn.sendall(data)  # 에코
