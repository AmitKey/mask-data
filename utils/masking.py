import re


def mask_credit_card(text):
    # Match any sequence of exactly 16 digits
    return re.sub(r'\b\d{16}\b', '***', text)


def mask_phone_number(text):
    # Match any sequence of exactly 9 digits
    return re.sub(r'\b\d{9}\b', '***', text)


def mask_ip_address(text):
    # Match an IP address (4 numbers 0-255 separated by dots)
    ip_pattern = (
        r'\b(?:'
        r'(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}'
        r'(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\b'
    )
    return re.sub(ip_pattern, '***', text)


def mask_sensitive_info(text):
    text = mask_credit_card(text)
    text = mask_phone_number(text)
    text = mask_ip_address(text)
    return text
