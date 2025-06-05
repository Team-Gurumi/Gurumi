# supply node wg0.conf
# [Interface]
# PrivateKey = <공급 노드 개인 키>
# Address = 10.0.0.1/24   # 공급 노드의 가상 IP
# ListenPort = 51820      # WireGuard 서버가 리스닝할 포트
#
# [Peer]
# PublicKey = <수요 노드 공개 키>
# AllowedIPs = 10.0.0.2/32  # 수요 노드 IP