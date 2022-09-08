import pytest
import time

from aleph_message.models import MessageType, MessagesResponse, PostMessage, PostContent
from build.lib.aleph_client import conf


from aleph_client.asynchronous import (
    get_messages,
    fetch_aggregates,
    fetch_aggregate,
    _get_fallback_session,
    create_post,
)

from aleph_client.chains.ethereum import ETHAccount, get_fallback_account


@pytest.mark.asyncio
async def test_fetch_aggregate():
    _get_fallback_session.cache_clear()

    response = await fetch_aggregate(
        address="0xa1B3bb7d2332383D96b7796B908fB7f7F3c2Be10", key="corechannel"
    )
    assert response.keys() == {"nodes", "resource_nodes"}


@pytest.mark.asyncio
async def test_fetch_aggregates():
    _get_fallback_session.cache_clear()

    response = await fetch_aggregates(
        address="0xa1B3bb7d2332383D96b7796B908fB7f7F3c2Be10"
    )
    assert response.keys() == {"corechannel"}
    assert response["corechannel"].keys() == {"nodes", "resource_nodes"}


@pytest.mark.asyncio
async def test_get_posts():
    _get_fallback_session.cache_clear()

    response: MessagesResponse = await get_messages(
        pagination=2,
        message_type=MessageType.post,
    )

    messages = response.messages
    assert len(messages) > 1
    for message in messages:
        assert message.type == MessageType.post


@pytest.mark.asyncio
async def test_get_messages():
    _get_fallback_session.cache_clear()

    response: MessagesResponse = await get_messages(
        pagination=2,
    )

    messages = response.messages
    assert len(messages) > 1
    assert messages[0].type
    assert messages[0].sender



@pytest.mark.asyncio
async def test_create_post():
    _get_fallback_session.cache_clear()
    
    account: ETHAccount = get_fallback_account()
    post_content : PostContent = (
        "ALEPH IN PARIS"
    )
    
    response: PostMessage = await create_post(
        account,
        post_content,
        post_type = "ok",
        ref = "02932831278",
        # address = conf.settings.ADDRESS_TO_USE,
        # channel = conf.settings.DEFAULT_CHANNEL,
        api_server = conf.settings.API_HOST,
        inline = True, 
    )
    
    content = response.content
    assert content.type == "ok"
    assert content.content == "ALEPH IN PARIS"
    assert content.time <= time.time()
    assert content.ref == "02932831278"
    
    # print(content)
        
    
    
