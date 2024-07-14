from utils.masking import mask_credit_card, mask_phone_number, mask_ip_address


def mask_sensitive_info(text):
    text = mask_credit_card(text)
    text = mask_phone_number(text)
    text = mask_ip_address(text)
    return text
