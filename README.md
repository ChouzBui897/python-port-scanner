# Python Port Scanner

A multi-threaded TCP Port Scanning & Service Detection tool developed in Python.

This project was developed as part of a Student Scientific Research project (2025–2026).

---

## Features

- TCP Connect Scan (`-sT`)
- TCP SYN Scan (`-sS`)
- Service Detection via Banner Grabbing
- Multi-threaded Scanning
- JSON Export Support
- Fast and Lightweight Architecture

---

## Technologies Used

- Python
- Socket Programming
- Threading
- JSON

---

## Scanning Techniques

### TCP Connect Scan
Establishes a full TCP connection to identify open ports.

### TCP SYN Scan
Performs half-open SYN scanning for faster detection.

### Banner Grabbing
Detects running services by analyzing service banners.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/ChouzBui897/python-port-scanner.git
cd python-port-scanner
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment (Windows)

```bash
.\venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Basic Scan

```bash
python main.py -t 192.168.1.1
```

---

### TCP Connect Scan

```bash
python main.py -t 192.168.1.1 -p 1-1000 -sT
```

---

### TCP SYN Scan

> Requires administrator/root privileges

```bash
sudo python main.py -t 192.168.1.1 -p 1-1000 -sS
```

---

### Multi-threaded Scan

```bash
python main.py -t 192.168.1.1 --threads 100
```

---

### Custom Timeout

```bash
python main.py -t 192.168.1.1 --timeout 2
```

---

### Export Results to JSON

```bash
python main.py -t 192.168.1.1 -oJ results.json
```

---

## Command Arguments

| Argument | Description |
|---|---|
| `-t`, `--target` | Target IP, CIDR, or file containing targets |
| `-p`, `--ports` | Port range or specific ports |
| `--threads` | Number of concurrent threads |
| `--timeout` | Connection timeout |
| `-sS` | TCP SYN Scan |
| `-sT` | TCP Connect Scan |
| `-oJ` | Export results to JSON |

---

## Example

```bash
sudo python main.py -t 192.168.1.1 -p 1-1000 -sS -oJ results.json
```

## Output Example

```json
{
    "192.168.1.1": [
        {
            "port": 22,
            "status": "open",
            "service": "ssh",
            "banner": "OpenSSH 8.2"
        },
        {
            "port": 80,
            "status": "open",
            "service": "http",
            "banner": "Apache/2.4.41"
        }
    ]
}
```

---

## Future Improvements

- UDP Scanning
- OS Detection
- Nmap-style Output
- GUI Interface
- Vulnerability Detection

---

## Author

Bui Minh Chau  
System Administration & DevOps Intern