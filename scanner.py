#!/usr/bin/env python3
"""
Advanced Network Scanner - Detailed Output
More aggressive scanning with verbose results
"""

import os
import subprocess
import sys
import time

def banner():
    print("\n" + "="*60)
    print("  🔍 ADVANCED NETWORK SCANNER - VERBOSE MODE")
    print("="*60 + "\n")

def display_file_content(filepath, title):
    """Display file content with a nice header"""
    if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
        print("\n" + "="*60)
        print(f"  📄 {title}")
        print("="*60)
        try:
            with open(filepath, 'r') as f:
                content = f.read()
                # Limit output to prevent overwhelming terminal
                lines = content.split('\n')
                if len(lines) > 50:
                    print('\n'.join(lines[:50]))
                    print(f"\n... ({len(lines) - 50} more lines)")
                    print(f"💡 View full file: cat {filepath}")
                else:
                    print(content)
        except Exception as e:
            print(f"[!] Could not read file: {e}")
        print("="*60)
    else:
        print(f"\n[!] {title}: No results or file not found")

def main():
    banner()
    
    # Get target
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = input("Enter target domain: ").strip()
    
    if not target:
        print("[!] No target specified")
        sys.exit(1)
    
    os.makedirs("output", exist_ok=True)
    
    print(f"\n[*] Target: {target}")
    print("[*] Running ADVANCED scan with detailed output\n")
    
    start = time.time()
    
    # ============================================
    # AMASS - More aggressive enumeration
    # ============================================
    print("[+] Amass (Active enumeration - 2min timeout)...")
    try:
        subprocess.run([
            "amass", "enum",
            "-d", target,
            "-active",           # Active enumeration (more aggressive)
            "-brute",            # Brute force subdomains
            "-w", "/usr/share/wordlists/amass/subdomains-top1mil-5000.txt",  # Wordlist
            "-timeout", "2",     # 2 minute timeout per source
            "-o", "output/subdomains.txt",
            "-v"                 # Verbose output
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
        
        if os.path.exists("output/subdomains.txt") and os.stat("output/subdomains.txt").st_size > 0:
            with open("output/subdomains.txt", 'r') as f:
                count = len(f.readlines())
            print(f"    [✓] Found {count} subdomain(s)")
        else:
            print("    [!] No subdomains found, using main domain")
            with open("output/subdomains.txt", "w") as f:
                f.write(target + "\n")
    except Exception as e:
        print(f"    [!] Amass error: {e}")
        with open("output/subdomains.txt", "w") as f:
            f.write(target + "\n")
    
    # ============================================
    # NMAP - Comprehensive port scan
    # ============================================
    print("\n[+] Nmap (Detailed scan - Service + OS + Scripts)...")
    try:
        subprocess.run([
            "nmap",
            "-iL", "output/subdomains.txt",
            "-sV",               # Service version detection
            "-sC",               # Default scripts
            "-O",                # OS detection
            "-A",                # Aggressive scan (OS, version, scripts, traceroute)
            "--top-ports", "1000",  # Top 1000 ports
            "-T4",               # Aggressive timing
            "--min-rate", "1000",   # Minimum packet rate
            "-oN", "output/nmap.txt",      # Normal output
            "-oX", "output/nmap.xml",      # XML output
            "--script", "vuln",  # Vulnerability scripts
            "-v"                 # Verbose
        ], timeout=300)
        print("    [✓] Nmap completed - Check nmap.txt and nmap.xml")
    except subprocess.TimeoutExpired:
        print("    [!] Nmap timeout (5min) - partial results saved")
    except Exception as e:
        print(f"    [!] Nmap error: {e}")
    
    # ============================================
    # WHATWEB - Aggressive web fingerprinting
    # ============================================
    print("\n[+] WhatWeb (Aggressive scan with all plugins)...")
    try:
        with open("output/whatweb.txt", "w") as f:
            subprocess.run([
                "whatweb",
                "-i", "output/subdomains.txt",
                "-a", "3",       # Aggression level 3 (most aggressive)
                "-v",            # Verbose output
                "--color=never", # No color codes in file
                "--log-verbose=output/whatweb_verbose.txt"  # Extra verbose log
            ], stdout=f, stderr=subprocess.DEVNULL, timeout=120)
        print("    [✓] WhatWeb completed - Check whatweb.txt and whatweb_verbose.txt")
    except subprocess.TimeoutExpired:
        print("    [!] WhatWeb timeout (2min)")
    except Exception as e:
        print(f"    [!] WhatWeb error: {e}")
    
    # ============================================
    # ADDITIONAL TOOLS (Optional but powerful)
    # ============================================
    
    # Nikto - Web vulnerability scanner
    print("\n[+] Nikto (Web vulnerability scan - Optional)...")
    try:
        subprocess.run([
            "nikto",
            "-h", target,
            "-o", "output/nikto.txt",
            "-Format", "txt"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180)
        print("    [✓] Nikto completed - Check nikto.txt")
    except:
        print("    [!] Nikto not available or timeout (install: sudo apt install nikto)")
    
    # SSLScan - SSL/TLS analysis
    print("\n[+] SSLScan (SSL/TLS analysis)...")
    try:
        with open("output/sslscan.txt", "w") as f:
            subprocess.run([
                "sslscan",
                "--no-colour",
                target
            ], stdout=f, stderr=subprocess.DEVNULL, timeout=60)
        print("    [✓] SSLScan completed - Check sslscan.txt")
    except:
        print("    [!] SSLScan not available (install: sudo apt install sslscan)")
    
    elapsed = time.time() - start
    
    # ============================================
    # SUMMARY
    # ============================================
    print("\n" + "="*60)
    print(f"[✓] SCAN COMPLETED in {elapsed:.1f} seconds!")
    print("="*60)
    print("\n📊 FILE SUMMARY:")
    print("-"*60)
    
    files = [
        ("Subdomains", "output/subdomains.txt"),
        ("Nmap Scan (Normal)", "output/nmap.txt"),
        ("Nmap Scan (XML)", "output/nmap.xml"),
        ("WhatWeb Results", "output/whatweb.txt"),
        ("WhatWeb Verbose", "output/whatweb_verbose.txt"),
        ("Nikto Scan", "output/nikto.txt"),
        ("SSL Scan", "output/sslscan.txt")
    ]
    
    for name, filepath in files:
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            if size > 0:
                print(f"  ✓ {name:20} : {filepath} ({size} bytes)")
            else:
                print(f"  ⚠ {name:20} : {filepath} (empty)")
        else:
            print(f"  ✗ {name:20} : Not created")
    
    print("-"*60)
    
    # ============================================
    # DISPLAY RESULTS IN TERMINAL
    # ============================================
    print("\n" + "="*60)
    print("  📊 SCAN RESULTS PREVIEW")
    print("="*60)
    
    # Display Subdomains
    display_file_content("output/subdomains.txt", "DISCOVERED SUBDOMAINS")
    
    # Display Nmap Results (first 50 lines)
    display_file_content("output/nmap.txt", "NMAP PORT SCAN RESULTS")
    
    # Display WhatWeb Results
    display_file_content("output/whatweb.txt", "WHATWEB TECHNOLOGY DETECTION")
    
    # Display Nikto if available
    if os.path.exists("output/nikto.txt") and os.path.getsize("output/nikto.txt") > 0:
        display_file_content("output/nikto.txt", "NIKTO VULNERABILITY SCAN")
    
    # Display SSL Scan if available
    if os.path.exists("output/sslscan.txt") and os.path.getsize("output/sslscan.txt") > 0:
        display_file_content("output/sslscan.txt", "SSL/TLS SECURITY ANALYSIS")
    
    # Final instructions
    print("\n" + "="*60)
    print("  💡 NEXT STEPS")
    print("="*60)
    print("\n📁 All results saved in: output/ directory")
    print("\n🔍 View full results:")
    print("    cat output/nmap.txt          # Full port scan")
    print("    cat output/subdomains.txt    # All subdomains")
    print("    cat output/whatweb.txt       # Web technologies")
    print("    cat output/nikto.txt         # Vulnerabilities")
    print("    cat output/sslscan.txt       # SSL/TLS info")
    print("\n📊 Open in browser:")
    print("    firefox output/nmap.xml      # Interactive view")
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Scan interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Unexpected error: {e}")
        sys.exit(1)
