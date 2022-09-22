import pytest
from dataclasses import dataclass, asdict

from aleph_client.chains.cosmos import CSDKAccount, get_fallback_account
from aleph_client.chains.common import delete_private_key_file


DEFAULT_HRP = "cosmos" 

@dataclass
class Message:
    chain: str
    sender: str
    type: str
    item_hash: str

def test_get_fallback_account():
    delete_private_key_file()
    account: CSDKAccount = get_fallback_account()

    assert account.CHAIN == "CSDK"
    assert account.CURVE == "secp256k1"
    assert account.hrp == DEFAULT_HRP
    

@pytest.mark.asyncio
async def test_CSDKAccount():
    
    account : CSDKAccount = get_fallback_account(hrp=DEFAULT_HRP)
    
    message = Message("CSDK", account.get_address(), "SomeType", "ItemHash")
    # signed = await account.sign_message(asdict(message))
    # # assert signed["signature"]
    # # assert len(signed["signature"]) == 253

    # address = account.get_address()
    # assert address
    # assert type(address) == str
    # assert len(address) == 45

    # pubkey = account.get_public_key()
    # assert type(pubkey) == bytes
    # assert len(pubkey) == 33
    
@pytest.mark.asyncio
async def test_decrypt_secp256k1():
    account: CSDKAccount = get_fallback_account(hrp=DEFAULT_HRP)

    assert account.CURVE == "secp256k1"
    content = b"SomeContent"

    # encrypted = await account.encrypt(content)
    # assert type(encrypted) == bytes
    # decrypted = await account.decrypt(encrypted)
    # assert type(decrypted) == bytes
    # assert content == decrypted