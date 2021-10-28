# TCP/IP socket programming
##### 소켓을 주소는 IPv4로 타입은 TCP로 생성
##### 포트 연결할 수 없다는 error 방지 코드 추가
##### Bind를 통하여 host와 port를 묶었으며 빈 문자열로 만들어 모든 ip의 접속 가능
##### Listen을 통하여 클라이언트의 접속을 가능하게 한 뒤 accept 함수를 통해서 클라이언트의 client_socket을 생성
##### 클라이언트의 message를 받은 뒤 메시지를 보낸 클라이언트의 주소와 함께 출력하고 메시지를 server message로 수정하여 전송
