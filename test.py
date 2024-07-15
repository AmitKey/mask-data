import pytest
from utils.masking import mask_credit_card, mask_phone_number, mask_ip_address


def test_mask_credit_card():
    # Arrange
    input_text = "My credit card number is 1234567891011120"
    expected_output = "My credit card number is ***"

    # Act
    result = mask_credit_card(input_text)

    # Assert
    assert result == expected_output


def test_mask_phone_number():
    # Arrange
    input_text = "Call me at 123456789"
    expected_output = "Call me at ***"

    # Act
    result = mask_phone_number(input_text)

    # Assert
    assert result == expected_output


def test_mask_ip_address():
    # Arrange
    input_text = "My IP is 192.180.1.1"
    expected_output = "My IP is ***"

    # Act
    result = mask_ip_address(input_text)

    # Assert
    assert result == expected_output

