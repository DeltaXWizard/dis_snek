from typing import Any, Dict, List, Optional, Union

from dis_snek.models.route import Route
from dis_snek.models.snowflake import Snowflake_Type


class MessageRequests:
    request: Any

    async def create_message(
        self,
        channel_id: Snowflake_Type,
        content: Optional[str],
        tts: Optional[bool] = False,
        embeds: Optional[List[Dict]] = None,
        components: Optional[List[dict]] = None,
    ) -> Any:
        """Send a message to the specified channel. Incomplete."""
        # todo: Complete this
        payload: Dict[str, Any] = {}

        if content:
            payload["content"] = content
        if tts:
            payload["tts"] = tts
        if embeds:
            payload["embeds"] = embeds
        if components:
            payload["components"] = components
        return await self.request(Route("POST", f"/channels/{channel_id}/messages"), json=payload)

    async def delete_message(self, channel_id: Snowflake_Type, message_id: Snowflake_Type, reason: str = None) -> Any:
        """Deletes a message from the specified channel. Incomplete."""
        await self.request(Route("DELETE", f"/channels/{channel_id}/messages/{message_id}"), reason=reason)

    async def get_message(self, channel_id: Snowflake_Type, message_id: Snowflake_Type) -> dict:
        """
        Get a specific message in the channel. Returns a message object on success.

        :param channel_id: the channel this message belongs to
        :param message_id: the id of the message
        :return: message or None
        """
        return await self.request(Route("GET", f"/channels/{channel_id}/messages/{message_id}"))

    async def pin_message(self, channel_id: Snowflake_Type, message_id: Snowflake_Type) -> None:
        """Pin a message to a channel

        :param channel_id: Channel to pin message to
        :param message_id: Message to pin
        """
        return await self.request(Route("PUT", f"/channels/{channel_id}/pins/{message_id}"))

    async def unpin_message(self, channel_id: Snowflake_Type, message_id: Snowflake_Type) -> None:
        """Unpin a message to a channel

        :param channel_id: Channel to unpin message to
        :param message_id: Message to unpin
        """
        return await self.request(Route("DELETE", f"/channels/{channel_id}/pins/{message_id}"))

    async def edit_message(
        self,
        channel_id: Snowflake_Type,
        message_id: Snowflake_Type,
        content: Optional[str],
        embeds: Optional[List[Dict]] = None,
        components: Optional[List[dict]] = None,
    ) -> dict:
        """Edit an existing message

        :param channel_id: Channel of message to edit
        :param message_id: Message to edit
        :param content: Content of the edit
        :param embeds: Message embeds
        :param components: Message components
        :return: Message object of edited message
        """
        # TODO: Add support for attachments, file, flags, allowed_mentions
        payload: Dict[str, Any] = {}

        if content:
            payload["content"] = content
        if embeds:
            payload["embeds"] = embeds
        if components:
            payload["components"] = components
        return await self.request(Route("PATCH", f"/channels/{channel_id}/messages/{message_id}"), json=payload)
