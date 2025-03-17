import hashlib
import argparse
import sys

def show_help():
    help_text = """
Gibbon Password Cracker - Brute forces a SHA-256 hash using a wordlist and salt.

Usage:
    python gibbon_cracker.py -w <wordlist> -s <salt> -H <hash>

Arguments:
    -w, --wordlist   Path to the wordlist file
    -s, --salt       Salt used in hashing
    -H, --hash       Target SHA-256 hash to crack

Example:
    python gibbon_cracker.py -w '/usr/share/wordlists/rockyou.txt' -s 'AbDfFgGiKlorRtTUy34579' -H '1d674dd4782f9b86e4014fe7e6feb916a5ee5bb674d7f61ecccbc496dbbcc04c'
"""
    print(help_text)
    sys.exit(1)

def crack_password(wordlist, salt, target_hash):
    try:
        with open(wordlist, "r", encoding="latin-1") as f:
            for password in f:
                password = password.strip()
                test_hash = hashlib.sha256((salt + password).encode()).hexdigest()
                if test_hash == target_hash:
                    print(f"[+] Password found: {password}")
                    return
        print("[-] Password not found.")
    except FileNotFoundError:
        print(f"[!] Error: Wordlist file '{wordlist}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-w", "--wordlist", required=False, help="Path to wordlist")
    parser.add_argument("-s", "--salt", required=False, help="Salt value")
    parser.add_argument("-H", "--hash", required=False, help="Target hash")

    args = parser.parse_args()

    if not (args.wordlist and args.salt and args.hash):
        show_help()

    crack_password(args.wordlist, args.salt, args.hash)
