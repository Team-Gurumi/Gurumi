# demand node wg0.conf
# [Interface]
# PrivateKey = <수요 노드 개인 키>
# Address = 10.0.0.2/24   # 수요 노드의 가상 IP
#
# [Peer]
# PublicKey = <공급 노드 공개 키>
# Endpoint = <공급 노드 IP>:51820   # 공급 노드 IP 및 포트
# AllowedIPs = 10.0.0.0/24    # 허용되는 네트워크 범위
# PersistentKeepalive = 25
