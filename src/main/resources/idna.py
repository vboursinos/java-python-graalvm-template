import idna

# Encode a non-ASCII domain name to ASCII (Punycode)
non_ascii_domain = "bücher.com"
ascii_domain = idna.encode(non_ascii_domain).decode('utf-8')

print(f"Original Domain: {non_ascii_domain}")
print(f"Encoded Domain (ASCII): {ascii_domain}")

# Decode an ASCII domain name back to the original non-ASCII format
decoded_domain = idna.decode(ascii_domain)

print(f"Decoded Domain (Original): {decoded_domain}")
