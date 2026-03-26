import socket

COMMON_PORTS = {
    21: "ftp", 22: "ssh", 23: "telnet", 25: "smtp", 53: "domain",
    80: "http", 111: "rpcbind", 139: "netbios-ssn", 443: "https",
    445: "microsoft-ds", 512: "exec", 513: "login", 514: "shell",
    1099: "rmiregistry", 1524: "ingreslock", 2121: "ccproxy-ftp",
    3306: "mysql", 5432: "postgresql", 8080: "http-proxy"
}

def get_service_name(port):
    """Tra cứu tên dịch vụ chuẩn từ số hiệu cổng."""
    try:
        return socket.getservbyport(port)
    except OSError:
        return COMMON_PORTS.get(port, "unknown")

def grab_banner(ip, port, timeout=2.0):
    """
    Thực hiện Banner Grabbing và định danh dịch vụ.
    Trả về một tuple: (service_name, banner_string)
    """
    service = get_service_name(port)
    banner = "Unknown"
    sock = None
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((ip, port))
        
        # Active Probing: Gửi yêu cầu TRƯỚC khi nhận đối với các cổng Web
        if port in [80, 443, 8080]:
            request = f"HEAD / HTTP/1.0\r\nHost: {ip}\r\n\r\n"
            sock.send(request.encode('utf-8'))
        
        raw_banner = sock.recv(1024)
        
        if raw_banner:
            # Xử lý chuỗi, lấy dòng đầu tiên của banner cho gọn gàng
            banner = raw_banner.decode('utf-8', errors='ignore').strip()
            banner = banner.split('\r\n')[0][:150] # Cắt ngắn nếu banner quá dài
            
    except Exception:
        # Giữ nguyên "Unknown" nếu gặp lỗi kết nối hoặc timeout
        pass
    finally:
        if sock:
            sock.close()
            
    return service, banner