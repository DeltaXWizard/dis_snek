from typing import Any, Dict, List, Optional, Union

from dis_snek.models.route import Route
from dis_snek.models.snowflake import Snowflake_Type


class ReactionRequests:
    request: Any

    async def create_reaction(self, channel_id: Snowflake_Type, message_id: Snowflake_Type, emoji: str) -> None:
        """
        Create a reaction for a message.

        :param channel_id: The channel this is taking place in
        :param message_id: The message to create a a reaction on
        :param emoji: The emoji to use (format: `name:id`)
        """
        return await self.request(
            Route(
                "PUT",
                "/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me",
                channel_id=channel_id,
                message_id=message_id,
                emoji=emoji,
            )
        )

    async def remove_self_reaction(self, channel_id: Snowflake_Type, message_id: Snowflake_Type, emoji: str) -> None:
        """
        Remove client's reaction from a message

        :param channel_id: The channel this is taking place in
        :param message_id: The message to create a a reaction on
        :param emoji: The emoji to remove (format: `name:id`)
        """
        return await self.request(
            Route(
                "DELETE",
                "/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me",
                channel_id=channel_id,
                message_id=message_id,
                emoji=emoji,
            )
        )

    async def remove_user_reaction(
        self, channel_id: Snowflake_Type, message_id: Snowflake_Type, emoji: str, user_id: Snowflake_Type
    ) -> None:
        """
        Remove user's reaction from a message

        :param channel_id: The channel this is taking place in
        :param message_id: The message to create a a reaction on
        :param emoji: The emoji to remove (format: `name:id`)
        :param user_id: The user to remove reaction of
        """
        return await self.request(
            Route(
                "DELETE",
                "/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/{user_id}",
                channel_id=channel_id,
                message_id=message_id,
                emoji=emoji,
                user_id=user_id,
            )
        )

    async def clear_reaction(self, channel_id: Snowflake_Type, message_id: Snowflake_Type, emoji: str) -> None:
        """
        Remove specific reaction from a message

        :param channel_id: The channel this is taking place in
        :param message_id: The message to create a a reaction on
        :param emoji: The emoji to remove (format: `name:id`)
        """
        return await self.request(
            Route(
                "DELETE",
                "/channels/{channel_id}/messages/{message_id}/reactions/{emoji}",
                channel_id=channel_id,
                message_id=message_id,
                emoji=emoji,
            )
        )

    async def clear_reactions(self, channel_id: Snowflake_Type, message_id: Snowflake_Type) -> None:
        """
        Remove reactions from a message.

        :param channel_id: The channel this is taking place in
        :param message_id: The message to clear reactions from
        """
        return await self.request(Route("DELETE", f"/channels/{channel_id}/messages/{message_id}/reactions"))
