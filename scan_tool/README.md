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

### TCP Connect Scan

```bash
python scanner.py -t 192.168.1.1 -sT
```

### TCP SYN Scan

```bash
python scanner.py -t 192.168.1.1 -sS
```

### Export JSON Result

```bash
python scanner.py -t 192.168.1.1 -json
```

---

## Output Example

```json
{
  "target": "192.168.1.1",
  "open_ports": [
    {
      "port": 80,
      "service": "HTTP"
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
