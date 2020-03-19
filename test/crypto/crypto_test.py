import os

from crypto.crypto_wrapper import CryptoWrapper


def get_bytes_from_file(filename):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), filename), 'rb') as f:
        return f.read()


def test_header_gen():
    ctr = get_bytes_from_file("ctr.bin")
    key = get_bytes_from_file("key.bin")
    header = get_bytes_from_file("header.bin")

    (my_header, my_key, my_ctr) = CryptoWrapper.generate_header(0x123)

    assert header == my_header

    assert key == my_key
    assert ctr == my_ctr


def test_encrypt_decrypt():
    data = bytes(b"0123456789")

    (header, enc_data) = CryptoWrapper.encrypt(data)

    dec_data = CryptoWrapper.decrypt(header, enc_data)

    assert data == dec_data


def test_decrypt_encrypt_decrypt_save():
    main = get_bytes_from_file("main.dat")
    header = get_bytes_from_file("mainHeader.dat")

    dec_data = CryptoWrapper.decrypt(header, main)

    (header2, enc_data) = CryptoWrapper.encrypt(dec_data)

    final_data = CryptoWrapper.decrypt(header2, enc_data)

    assert final_data == get_bytes_from_file("main_dec.dat")
