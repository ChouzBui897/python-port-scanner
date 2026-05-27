import json

def print_console(results):
    """
    In kết quả quét đẹp mắt ra màn hình.
    """
    print("\n" + "="*80)
    print(f"{'IP Address':<15} | {'Port':<7} | {'Status':<8} | {'Service':<15} | {'Banner'}")
    print("-" * 80)
    
    for host, host_results in results.items():
        for p_res in host_results:
            port = p_res.get('port', 'N/A')
            status = p_res.get('status', 'N/A')
            service = p_res.get('service', 'unknown')
            banner = p_res.get('banner', 'Unknown')
            
            print(f"{host:<15} | {port:<7} | {status:<8} | {service:<15} | {banner}")
    print("="*80 + "\n")

def save_json(results, filename):
    """
    Lưu kết quả quét ra file định dạng JSON.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=4, ensure_ascii=False)
        print(f"[+] Kết quả JSON hoàn chỉnh đã được lưu tại: {filename}")
    except Exception as e:
        print(f"[-] Lỗi khi lưu file JSON: {e}")