import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
import input_parser
import target_manager
import scanning_engine
import service_detector
import reporter

def check_privileges():
    """Kiểm tra quyền root/admin nếu chạy SYN Scan."""
    try:
        # Kiểm tra trên Linux/Unix
        if os.name != 'nt':
            return os.geteuid() == 0
        # Trên Windows, Scapy sẽ báo lỗi nếu không có quyền Admin
        return True 
    except AttributeError:
        return False

def scan_task(ip, port, scan_type, timeout):
    """Nhiệm vụ quét cho từng cổng cụ thể."""
    if scan_type == "SYN":
        status = scanning_engine.syn_scan(ip, port, timeout)
    else:
        status = scanning_engine.connect_scan(ip, port, timeout)
    
    # Khởi tạo result mặc định
    result = {"port": port, "status": status, "service": "unknown", "banner": "N/A"}
    
    if status == "open":
        service_name, banner_info = service_detector.grab_banner(ip, port, timeout)
        result["service"] = service_name
        result["banner"] = banner_info
    
    return ip, result

def main():
    args = input_parser.parse_args()
    
    if args.scan_type == "SYN" and not check_privileges():
        print("[-] Lỗi: SYN Scan yêu cầu quyền Root/Administrator.")
        sys.exit(1)

    ip_list = target_manager.parse_targets(args.target)
    port_list = target_manager.parse_ports(args.ports)
    
    if not ip_list or not port_list:
        print("[-] Không tìm thấy mục tiêu hoặc cổng hợp lệ để quét.")
        sys.exit(1)

    print(f"[*] Bắt đầu quét {len(ip_list)} mục tiêu với {args.threads} luồng...")
    print(f"[*] Kiểu quét: {args.scan_type}, Timeout: {args.timeout}s")

    final_results = {ip: [] for ip in ip_list}
    
    # 4. Thực thi đa luồng
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = []
        for ip in ip_list:
            for port in port_list:
                futures.append(executor.submit(scan_task, ip, port, args.scan_type, args.timeout))
        
        for future in as_completed(futures):
            ip, res = future.result()
            if res["status"] == "open": 
                final_results[ip].append(res)

    # 5. Xuất kết quả
    reporter.print_console(final_results)
    
    if args.output_json:
        reporter.save_json(final_results, args.output_json)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Người dùng dừng quá trình quét.")
        sys.exit(0)