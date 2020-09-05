import socket


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 소켓 핸들러 생성
mysock.connect(('data.pr4e.org', 80))
# 소켓연결 호스트, 포트
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# HTTP 프로토콜 규칙에 따라 데이터를 요청
# HTTP 프로토콜의 "GET" 사용하는 경우 끝에 공백라인 한줄을 붙여서 보내라는 규칙이 있음
# encode() : Unicode string -> UTF-8 bytes
# -> cmd is a bytes.
mysock.send(cmd)
# 요청한 데이터를 소켓으로 보냄(문자열 전송)

while True:
    data = mysock.recv(512)
	# 서버에서 받은 데이터를 data 변수에 저장
    # 데이터 버퍼 크기: 512
    if (len(data) < 1):
        break
    print(data.decode())
    # UTF-8 형식 -> Unicode
mysock.close()
# 소켓 닫음

