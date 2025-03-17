# 🦍 Gibbon Password Cracker  

A simple SHA-256 password cracker that brute forces a salted hash using a wordlist.  

## 📌 Features  
- Uses **SHA-256** hashing algorithm.  
- Supports **custom wordlists**.  
- Accepts **custom salt values**.  
- **Simple & lightweight**, no dependencies.  

## 🔧 Usage  
```sh
python gibbon_cracker.py -w <wordlist> -s <salt> -H <hash>
```
## 🔹 Arguments

| Flag   | Description               | Example                                      |
|--------|---------------------------|----------------------------------------------|
| `-w`   | Path to the wordlist file | `/usr/share/wordlists/rockyou.txt`           |
| `-s`   | Salt used in hashing      | `'AbDfFgGiKlorRtTUy34579'`                  |
| `-H`   | Target SHA-256 hash       | `'1d674dd4782f9b86e4014fe7e6feb916a5ee5bb674d7f61ecccbc496dbbcc04c'` |

## 🔹 Example
```sh
python gibbon_cracker.py -w '/usr/share/wordlists/rockyou.txt' -s 'AbDfFgGiKlorRtTUy34579' -H '1d674dd4782f9b86e4014fe7e6feb916a5ee5bb674d7f61ecccbc496dbbcc04c'
```

## ⚠️ Notes
This script does not support multi-threading.
Make sure the wordlist file exists before running the script.
If no password is found, the script will print [-] Password not found.
