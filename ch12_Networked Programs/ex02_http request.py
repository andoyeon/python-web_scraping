import socket


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 소켓 핸들러 생성
mysock.connect(('data.pr4e.org', 80))
# 소켓연결 호스트, 포트
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# HTTP 프로토콜의 "GET" 커맨드를 사용하는 경우
# 끝에 공백라인 한줄을 붙여서 보내라는 규칙이 있음
mysock.send(cmd)
# 문자열 전송

while True:
    data = mysock.recv(512)
    # 데이터 버퍼 크기: 512
    if (len(data) < 1):
        break
    print(data.decode())
    # UTF-8 형식 -> 유니코드
mysock.close()
# 소켓 닫음

