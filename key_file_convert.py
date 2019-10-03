import sys

from eth_keyfile import extract_key_from_keyfile
from eth_utils import encode_hex
from getpass import getpass

key_file_path = sys.argv[1]
account_balance = '100000000000000000000'


def get_private_key(key_file_path, password):
    """Gets private key from ethereum key file

    Args:
        key_file_path: path to the ethereum key file
        password: password to decrypt the file

    Returns:
        [str]: hex encoded private key
    """
    private_key_bytes = extract_key_from_keyfile(key_file_path, password)

    return encode_hex(private_key_bytes)


def ganache_account_option(private_key, balance):
    """Generates ganache-cli account option with private key and balance

    Output format: `--account="<private_key>,balance"`

    Args:
        private_key (str): hex encoded private key (0x prefixed)
        balance ([str|int]): required balance for account in wei

    Returns:
        [str]: Formated account option
    """
    return f'--account=\"{private_key},{balance}"'


password = getpass()

private_key = get_private_key(key_file_path, password)

print(f"Private key:\n{private_key}")

account_option = ganache_account_option(private_key, account_balance)

print(f"Ganache argument:\n{account_option}")
