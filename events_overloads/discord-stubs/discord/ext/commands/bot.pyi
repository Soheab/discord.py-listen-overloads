import discord
from discord.ext.commands.core import GroupMixin  # type: ignore

from typing import Callable, Union, overload, Literal, TypeVar, Coroutine, Any

from events_enum import Event, PossibleEvents, PossibleEventsWithOn
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
        name: Literal[
            "on_app_command_completion",
            "app_command_completion",
            Event.AppCommandCompletion,
        ] = ...,
    ) -> EventCallable[app_commands.ApplicationCommandCompletionEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_raw_app_command_permissions_update",
            "raw_app_command_permissions_update",
            Event.RawAppCommandPermissionsUpdate,
        ] = ...,
    ) -> EventCallable[app_commands.RawApplicationCommandPermissionsUpdateEvent]: ...

    # --- Automod ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_automod_action",
            "automod_action",
            Event.AutoModAction,
        ],
    ) -> EventCallable[automod.AutoModActionEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_automod_rule_create",
            "automod_rule_create",
            Event.AutoModRuleCreate,
            "on_automod_rule_update",
            "automod_rule_update",
            Event.AutoModRuleUpdate,
            "on_automod_rule_delete",
            "automod_rule_delete",
            Event.AutoModRuleDelete,
        ] = ...,
    ) -> EventCallable[automod.AutoModRuleEvents]: ...

    # --- Channels ---
    @overload
    def listen(
        self,
        name: Literal[
            "on_guild_channel_create",
            "guild_channel_create",
            Event.GuildChannelCreate,
            "on_guild_channel_delete",
            "guild_channel_delete",
            Event.GuildChannelDelete,
        ],
    ) -> EventCallable[channels.GuildChannelCreateDeleteEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_guild_channel_update",
            "guild_channel_update",
            Event.GuildChannelUpdate,
        ],
    ) -> EventCallable[channels.GuildChannelUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_guild_channel_pins_update",
            "guild_channel_pins_update",
            Event.GuildChannelPinsUpdate,
        ],
    ) -> EventCallable[channels.GuildChannelPinsUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_private_channel_update",
            "private_channel_update",
            Event.PrivateChannelUpdate,
        ],
    ) -> EventCallable[channels.PrivateChannelUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_private_channel_pins_update",
            "private_channel_pins_update",
            Event.PrivateChannelPinsUpdate,
        ],
    ) -> EventCallable[channels.PrivateChannelPinsUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_typing",
            "typing",
            Event.Typing,
        ],
    ) -> EventCallable[channels.TypingEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_raw_typing",
            "raw_typing",
            Event.RawTyping,
        ],
    ) -> EventCallable[channels.RawTypingEvent]: ...

    # --- Connection ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_connect",
            "connect",
            Event.Connect,
        ],
    ) -> EventCallable[connection.ConnectEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_disconnect",
            "disconnect",
            Event.Disconnect,
        ],
    ) -> EventCallable[connection.DisconnectEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_shard_connect",
            "shard_connect",
            Event.ShardConnect,
            "on_shard_disconnect",
            "shard_disconnect",
            Event.ShardDisconnect,
            # gateway
            "on_shard_ready",
            "shard_ready",
            Event.ShardReady,
            "on_shard_resumed",
            "shard_resumed",
            Event.ShardResumed,
        ],
    ) -> EventCallable[connection.ShardEvent]: ...

    # --- Debug ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_error",
            "error",
            Event.Error,
        ],
    ) -> EventCallable[debug.ErrorEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_socket_event_type",
            "socket_event_type",
            Event.SocketEventType,
        ],
    ) -> EventCallable[debug.SocketEventTypeEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_socket_raw_receive",
            "socket_raw_receive",
            Event.SocketRawReceive,
        ],
    ) -> EventCallable[debug.SocketRawReceiveEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_socket_raw_send",
            "socket_raw_send",
            Event.SocketRawSend,
        ],
    ) -> EventCallable[debug.SocketRawSendEvent]: ...

    # --- Entitlements ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_entitlement_create",
            "entitlement_create",
            Event.EntitlementCreate,
            "on_entitlement_delete",
            "entitlement_delete",
            Event.EntitlementDelete,
            "on_entitlement_update",
            "entitlement_update",
            Event.EntitlementUpdate,
        ],
    ) -> EventCallable[entitlements.EntitlementEvent]: ...

    # --- Gateway ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_ready",
            "ready",
            Event.Ready,
        ],
    ) -> EventCallable[gateway.ReadyEvent]: ...

    # --- Guilds ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_guild_available",
            "guild_available",
            Event.GuildAvailable,
            "on_guild_unavailable",
            "guild_unavailable",
            Event.GuildUnavailable,
            "on_guild_join",
            "guild_join",
            Event.GuildJoin,
            "on_guild_remove",
            "guild_remove",
            Event.GuildRemove,
            # integrations
            "on_guild_integrations_update",
            "guild_integrations_update",
            Event.GuildIntegrationsUpdate,
        ],
    ) -> EventCallable[guilds.GuildEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_guild_update",
            "guild_update",
            Event.GuildUpdate,
        ],
    ) -> EventCallable[guilds.GuildUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_guild_emojis_update",
            "guild_emojis_update",
            Event.GuildEmojisUpdate,
        ],
    ) -> EventCallable[guilds.GuildEmojisUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_guild_stickers_update",
            "guild_stickers_update",
            Event.GuildStickersUpdate,
        ],
    ) -> EventCallable[guilds.GuildStickersUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_audit_log_entry_create",
            "audit_log_entry_create",
            Event.AuditLogEntryCreate,
        ],
    ) -> EventCallable[guilds.AuditLogEntryCreateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_invite_create",
            "invite_create",
            Event.InviteCreate,
            "on_invite_delete",
            "invite_delete",
            Event.InviteDelete,
        ],
    ) -> EventCallable[guilds.InviteEvent]: ...

    # --- Integrations ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_integration_create",
            "integration_create",
            Event.IntegrationCreate,
            "on_integration_update",
            "integration_update",
            Event.IntegrationUpdate,
        ],
    ) -> EventCallable[integrations.IntegrationEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_webhooks_update",
            "webhooks_update",
            Event.WebhooksUpdate,
        ],
    ) -> EventCallable[integrations.WebhooksUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_raw_integration_delete",
            "raw_integration_delete",
            Event.RawIntergrationDelete,
        ],
    ) -> EventCallable[integrations.RawIntegrationDeleteEvent]: ...

    # --- Interactions ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_interaction",
            "interaction",
            Event.Interaction,
        ],
    ) -> EventCallable[interactions.InteractionEvent]: ...

    # --- Members ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_member_join",
            "member_join",
            Event.MemberJoin,
            "on_member_remove",
            "member_remove",
            Event.MemberRemove,
        ],
    ) -> EventCallable[members.MemberEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_raw_member_remove",
            "raw_member_remove",
            Event.RawMemberRemove,
        ],
    ) -> EventCallable[members.RawMemberRemoveEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_member_update",
            "member_update",
            Event.MemberUpdate,
            # presence
            "on_presence_update",
            "presence_update",
            Event.PresenceUpdate,
        ],
    ) -> EventCallable[members.MemberUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_user_update",
            "user_update",
            Event.UserUpdate,
        ],
    ) -> EventCallable[members.UserUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_member_ban",
            "member_ban",
            Event.MemberBan,
        ],
    ) -> EventCallable[members.MemberBanEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_member_unban",
            "member_unban",
            Event.MemberUnban,
        ],
    ) -> EventCallable[members.MemberUnbanEvent]: ...

    # --- Messages ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_message",
            "message",
            Event.Message,
            # delete
            "on_message_delete",
            "message_delete",
            Event.MessageDelete,
        ],
    ) -> EventCallable[messages.MessageEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_message_edit",
            "message_edit",
            Event.MessageEdit,
        ],
    ) -> EventCallable[messages.MessageEditEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_bulk_message_delete",
            "bulk_message_delete",
            Event.BulkMessageDelete,
        ],
    ) -> EventCallable[messages.BulkMessageDeleteEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_raw_message_edit",
            "raw_message_edit",
            Event.RawMessageEdit,
        ],
    ) -> EventCallable[messages.RawMessageEditEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_raw_message_delete",
            "raw_message_delete",
            Event.RawMessageDelete,
        ],
    ) -> EventCallable[messages.RawMessageDeleteEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_raw_bulk_message_delete",
            "raw_bulk_message_delete",
            Event.RawBulkMessageDelete,
        ],
    ) -> EventCallable[messages.RawBulkMessageDeleteEvent]: ...

    # --- Reactions ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_reaction_add",
            "reaction_add",
            Event.ReactionAdd,
            "on_reaction_remove",
            "reaction_remove",
            Event.ReactionRemove,
        ],
    ) -> EventCallable[reactions.ReactionEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_reaction_clear",
            "reaction_clear",
            Event.ReactionClear,
        ],
    ) -> EventCallable[reactions.ReactionClearEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_reaction_clear_emoji",
            "reaction_clear_emoji",
            Event.ReactionClearEmoji,
        ],
    ) -> EventCallable[reactions.ReactionClearEmojiEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_raw_reaction_add",
            "raw_reaction_add",
            Event.RawReactionAdd,
            "on_raw_reaction_remove",
            "raw_reaction_remove",
            Event.RawReactionRemove,
        ],
    ) -> EventCallable[reactions.RawReactionActionEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_raw_reaction_clear",
            "raw_reaction_clear",
            Event.RawReactionClear,
        ],
    ) -> EventCallable[reactions.RawReactionClearEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_raw_reaction_clear_emoji",
            "raw_reaction_clear_emoji",
            Event.RawReactionClearEmoji,
        ],
    ) -> EventCallable[reactions.RawReactionClearEmojiEvent]: ...

    # --- Roles ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_guild_role_create",
            "guild_role_create",
            Event.GuildRoleCreate,
            "on_guild_role_delete",
            "guild_role_delete",
            Event.GuildRoleDelete,
        ],
    ) -> EventCallable[roles.GuildRoleEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_guild_role_update",
            "guild_role_update",
            Event.GuildRoleUpdate,
        ],
    ) -> EventCallable[roles.GuildRoleUpdateEvent]: ...

    # --- Scheduled Events ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_scheduled_event_create",
            "scheduled_event_create",
            Event.ScheduledEventCreate,
            "on_scheduled_event_delete",
            "scheduled_event_delete",
            Event.ScheduledEventDelete,
        ],
    ) -> EventCallable[scheduled_events.ScheduledEventEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_scheduled_event_update",
            "scheduled_event_update",
            Event.ScheduledEventUpdate,
        ],
    ) -> EventCallable[scheduled_events.ScheduledEventUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_scheduled_event_user_add",
            "scheduled_event_user_add",
            Event.ScheduledEventUserAdd,
            "on_scheduled_event_user_remove",
            "scheduled_event_user_remove",
            Event.ScheduledEventUserRemove,
        ],
    ) -> EventCallable[scheduled_events.ScheduledEventUserEvent]: ...

    # --- Stages ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_stage_instance_create",
            "stage_instance_create",
            Event.StageInstanceCreate,
            "on_stage_instance_delete",
            "stage_instance_delete",
            Event.StageInstanceDelete,
        ],
    ) -> EventCallable[stages.StageInstanceEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_stage_instance_update",
            "stage_instance_update",
            Event.StageInstanceUpdate,
        ],
    ) -> EventCallable[stages.StageInstanceUpdateEvent]: ...

    # --- Threads ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_thread_create",
            "thread_create",
            Event.ThreadCreate,
            "on_thread_join",
            "thread_join",
            Event.ThreadJoin,
            "on_thread_remove",
            "thread_remove",
            Event.ThreadRemove,
            "on_thread_delete",
            "thread_delete",
            Event.ThreadDelete,
        ],
    ) -> EventCallable[threads.ThreadEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_thread_update",
            "thread_update",
            Event.ThreadUpdate,
        ],
    ) -> EventCallable[threads.ThreadUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_raw_thread_update",
            "raw_thread_update",
            Event.RawThreadUpdate,
        ],
    ) -> EventCallable[threads.RawThreadUpdateEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_raw_thread_delete",
            "raw_thread_delete",
            Event.RawThreadDelete,
        ],
    ) -> EventCallable[threads.RawThreadDeleteEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_thread_member_join",
            "thread_member_join",
            Event.ThreadMemberJoin,
            "on_thread_member_remove",
            "thread_member_remove",
            Event.ThreadMemberRemove,
        ],
    ) -> EventCallable[threads.ThreadMemberEvent]: ...
    @overload
    def listen(
        self,
        name: Literal[
            "on_raw_thread_member_remove",
            "raw_thread_member_remove",
            Event.RawThreadMemberRemove,
        ],
    ) -> EventCallable[threads.RawThreadMemberRemoveEvent]: ...

    # --- Voice ---

    @overload
    def listen(
        self,
        name: Literal[
            "on_voice_state_update",
            "voice_state_update",
            Event.VoiceStateUpdate,
        ],
    ) -> EventCallable[voice.VoiceStateUpdateEvent]: ...

    # fmt: off
    def listen(
        self,
        name: Union[Event, PossibleEventsWithOn, PossibleEvents] = ...,
    ) -> Callable[[CoroFunc], CoroFunc]: ...
    # fmt: on

class Bot(BotBase, discord.Client): ...
class AutoShardedBot(BotBase, discord.AutoShardedClient): ...
