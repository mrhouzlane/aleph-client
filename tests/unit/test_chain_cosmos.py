from aleph_client.chains.cosmos import CSDKAccount, get_fallback_account
from aleph_client.chains.common import delete_private_key_file

DEFAULT_HRP = 'cosmos' 

def test_get_fallback_account():
    delete_private_key_file()
    account: CSDKAccount = get_fallback_account()

    assert account.CHAIN == "CSDK"
    assert account.CURVE == "secp256k1"
    assert account.hrp == DEFAULT_HRP
    
    