import discord
from discord.ext.commands.core import GroupMixin  # type: ignore

from typing import Callable, overload, Literal, TypeVar, Coroutine, Any

from events_enum import PossibleEventsWithOn
from protocols import (
    app_commands,
    automod,
    channels,
    connection,
    debug,
    entitlements,
    gateway,
    guilds,
    integrations,
    interactions,
    members,
    messages,
    reactions,
    roles,
    scheduled_events,
    stages,
    threads,
    voice,
)

CoroFunc = Callable[..., Coroutine[Any, Any, Any]]
EventT = TypeVar("EventT")
EventCallable = Callable[[EventT], EventT]

class BotBase(GroupMixin[None]):
    @overload
    def listen(
        self,
        name: Literal["on_app_command_completion",] = ...,
    ) -> EventCallable[app_commands.ApplicationCommandCompletionEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_raw_app_command_permissions_update",] = ...,
    ) -> EventCallable[app_commands.RawApplicationCommandPermissionsUpdateEvent]: ...

    # --- Automod ---

    @overload
    def listen(
        self,
        name: Literal["on_automod_action",],
    ) -> EventCallable[automod.AutoModActionEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_automod_rule_create",
            "on_automod_rule_update",
            "on_automod_rule_delete",
        ] = ...,
    ) -> EventCallable[automod.AutoModRuleEvents]: ...

    # --- Channels ---
    @overload
    def listen(
        self,
        name: Literal[
            "on_guild_channel_create",
            "on_guild_channel_delete",
        ],
    ) -> EventCallable[channels.GuildChannelCreateDeleteEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_guild_channel_update",],
    ) -> EventCallable[channels.GuildChannelUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_guild_channel_pins_update",],
    ) -> EventCallable[channels.GuildChannelPinsUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_private_channel_update",],
    ) -> EventCallable[channels.PrivateChannelUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_private_channel_pins_update",],
    ) -> EventCallable[channels.PrivateChannelPinsUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_typing",],
    ) -> EventCallable[channels.TypingEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_raw_typing",],
    ) -> EventCallable[channels.RawTypingEvent]: ...

    # --- Connection ---

    @overload
    def listen(
        self,
        name: Literal["on_connect",],
    ) -> EventCallable[connection.ConnectEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_disconnect",],
    ) -> EventCallable[connection.DisconnectEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_shard_connect",
            "on_shard_disconnect",
            # gateway
            "on_shard_ready",
            "on_shard_resumed",
        ],
    ) -> EventCallable[connection.ShardEvent]: ...

    # --- Debug ---

    @overload
    def listen(
        self,
        name: Literal["on_error",],
    ) -> EventCallable[debug.ErrorEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_socket_event_type",],
    ) -> EventCallable[debug.SocketEventTypeEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_socket_raw_receive",],
    ) -> EventCallable[debug.SocketRawReceiveEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_socket_raw_send",],
    ) -> EventCallable[debug.SocketRawSendEvent]: ...

    # --- Entitlements ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_entitlement_create",
            "on_entitlement_delete",
            "on_entitlement_update",
        ],
    ) -> EventCallable[entitlements.EntitlementEvent]: ...

    # --- Gateway ---

    @overload
    def listen(
        self,
        name: Literal["on_ready",],
    ) -> EventCallable[gateway.ReadyEvent]: ...

    # --- Guilds ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_guild_available",
            "on_guild_unavailable",
            "on_guild_join",
            "on_guild_remove",
            # integrations
            "on_guild_integrations_update",
        ],
    ) -> EventCallable[guilds.GuildEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_guild_update",],
    ) -> EventCallable[guilds.GuildUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_guild_emojis_update",],
    ) -> EventCallable[guilds.GuildEmojisUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_guild_stickers_update",],
    ) -> EventCallable[guilds.GuildStickersUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_audit_log_entry_create",],
    ) -> EventCallable[guilds.AuditLogEntryCreateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_invite_create",
            "on_invite_delete",
        ],
    ) -> EventCallable[guilds.InviteEvent]: ...

    # --- Integrations ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_integration_create",
            "on_integration_update",
        ],
    ) -> EventCallable[integrations.IntegrationEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_webhooks_update",],
    ) -> EventCallable[integrations.WebhooksUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_raw_integration_delete",],
    ) -> EventCallable[integrations.RawIntegrationDeleteEvent]: ...

    # --- Interactions ---

    @overload
    def listen(
        self,
        name: Literal["on_interaction",],
    ) -> EventCallable[interactions.InteractionEvent]: ...

    # --- Members ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_member_join",
            "on_member_remove",
        ],
    ) -> EventCallable[members.MemberEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_raw_member_remove",],
    ) -> EventCallable[members.RawMemberRemoveEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_member_update",
            # presence
            "on_presence_update",
        ],
    ) -> EventCallable[members.MemberUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_user_update",],
    ) -> EventCallable[members.UserUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_member_ban",],
    ) -> EventCallable[members.MemberBanEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_member_unban",],
    ) -> EventCallable[members.MemberUnbanEvent]: ...

    # --- Messages ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_message",
            # delete
            "on_message_delete",
        ],
    ) -> EventCallable[messages.MessageEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_message_edit",],
    ) -> EventCallable[messages.MessageEditEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_bulk_message_delete",],
    ) -> EventCallable[messages.BulkMessageDeleteEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_raw_message_edit",],
    ) -> EventCallable[messages.RawMessageEditEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_raw_message_delete",],
    ) -> EventCallable[messages.RawMessageDeleteEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_raw_bulk_message_delete",],
    ) -> EventCallable[messages.RawBulkMessageDeleteEvent]: ...

    # --- Reactions ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_reaction_add",
            "on_reaction_remove",
        ],
    ) -> EventCallable[reactions.ReactionEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_reaction_clear",],
    ) -> EventCallable[reactions.ReactionClearEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_reaction_clear_emoji",],
    ) -> EventCallable[reactions.ReactionClearEmojiEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_raw_reaction_add",
            "on_raw_reaction_remove",
        ],
    ) -> EventCallable[reactions.RawReactionActionEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_raw_reaction_clear",],
    ) -> EventCallable[reactions.RawReactionClearEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_raw_reaction_clear_emoji",],
    ) -> EventCallable[reactions.RawReactionClearEmojiEvent]: ...

    # --- Roles ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_guild_role_create",
            "on_guild_role_delete",
        ],
    ) -> EventCallable[roles.GuildRoleEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_guild_role_update",],
    ) -> EventCallable[roles.GuildRoleUpdateEvent]: ...

    # --- Scheduled Events ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_scheduled_event_create",
            "on_scheduled_event_delete",
        ],
    ) -> EventCallable[scheduled_events.ScheduledEventEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_scheduled_event_update",],
    ) -> EventCallable[scheduled_events.ScheduledEventUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_scheduled_event_user_add",
            "on_scheduled_event_user_remove",
        ],
    ) -> EventCallable[scheduled_events.ScheduledEventUserEvent]: ...

    # --- Stages ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_stage_instance_create",
            "on_stage_instance_delete",
        ],
    ) -> EventCallable[stages.StageInstanceEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_stage_instance_update",],
    ) -> EventCallable[stages.StageInstanceUpdateEvent]: ...

    # --- Threads ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_thread_create",
            "on_thread_join",
            "on_thread_remove",
            "on_thread_delete",
        ],
    ) -> EventCallable[threads.ThreadEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_thread_update",],
    ) -> EventCallable[threads.ThreadUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_raw_thread_update",],
    ) -> EventCallable[threads.RawThreadUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_raw_thread_delete",],
    ) -> EventCallable[threads.RawThreadDeleteEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_thread_member_join",
            "on_thread_member_remove",
        ],
    ) -> EventCallable[threads.ThreadMemberEvent]: ...
    @overload
    def listen(
        self,
        name: Literal["on_raw_thread_member_remove",],
    ) -> EventCallable[threads.RawThreadMemberRemoveEvent]: ...

    # --- Voice ---

    @overload
    def listen(
        self,
        name: Literal["on_voice_state_update",],
    ) -> EventCallable[voice.VoiceStateUpdateEvent]: ...

    # -- Default --

    def listen(
        self,
        name: PossibleEventsWithOn = ...,
    ) -> Callable[[CoroFunc], CoroFunc]: ...

class Bot(BotBase, discord.Client): ...
class AutoShardedBot(BotBase, discord.AutoShardedClient): ...
