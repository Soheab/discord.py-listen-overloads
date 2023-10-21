from typing import Literal

from enum import Enum

PossibleEventsWithOn = Literal[
    # App commands
    "on_raw_app_command_permissions_update",
    "on_app_command_completion",
    # AutoMod
    "on_automod_rule_create",
    "on_automod_rule_delete",
    "on_automod_rule_update",
    "on_automod_action",
    # Channels
    "on_guild_channel_delete",
    "on_guild_channel_update",
    "on_guild_channel_create",
    "on_guild_channel_pins_update",
    "on_private_channel_update",
    "on_private_channel_pins_update",
    "on_typing",
    "on_raw_typing",
    # Connection
    "on_connect",
    "on_disconnect",
    "on_shard_connect",
    "on_shard_disconnect",
    # Debug
    "on_error",  # This is not a real event
    "on_socket_event_type",
    "on_socket_raw_receive",
    "on_socket_raw_send",
    # Entitlements
    "on_entitlement_create",
    "on_entitlement_delete",
    "on_entitlement_update",
    # Gateway
    "on_ready",
    "on_resumed",
    "on_shard_ready",
    "on_shard_resumed",
    # Guilds
    "on_guild_available",
    "on_guild_unavailable",
    "on_guild_join",
    "on_guild_remove",
    "on_guild_update",
    "on_guild_emojis_update",
    "on_guild_stickers_update",
    "on_audit_log_entry_create",
    "on_invite_create",
    "on_invite_delete",
    # Integrations
    "on_integration_create",
    "on_integration_update",
    "on_guild_integrations_update",
    "on_webhooks_update",
    "on_raw_integration_delete",
    # Interactions
    "on_interaction",
    # Members
    "on_member_join",
    "on_member_remove",
    "on_raw_member_remove",
    "on_member_update",
    "on_user_update",
    "on_member_ban",
    "on_member_unban",
    "on_presence_update",
    # Messages
    "on_message",
    "on_message_edit",
    "on_message_delete",
    "on_bulk_message_delete",
    "on_raw_message_edit",
    "on_raw_message_delete",
    "on_raw_bulk_message_delete",
    # Reactions
    "on_reaction_add",
    "on_reaction_remove",
    "on_reaction_clear",
    "on_reaction_clear_emoji",
    "on_raw_reaction_add",
    "on_raw_reaction_remove",
    "on_raw_reaction_clear",
    "on_raw_reaction_clear_emoji",
    # Roles
    "on_guild_role_create",
    "on_guild_role_delete",
    "on_guild_role_update",
    # Scheduled Events
    "on_scheduled_event_create",
    "on_scheduled_event_update",
    "on_scheduled_event_delete",
    "on_scheduled_event_user_add",
    "on_scheduled_event_user_remove",
    # Stages
    "on_stage_instance_create",
    "on_stage_instance_delete",
    "on_stage_instance_update",
    # Threads
    "on_thread_create",
    "on_thread_join",
    "on_thread_update",
    "on_thread_remove",
    "on_thread_delete",
    "on_raw_thread_update",
    "on_raw_thread_delete",
    "on_thread_member_join",
    "on_thread_member_remove",
    "on_raw_thread_member_remove",
    # Voice
    "on_voice_state_update",
]

PossibleEvents = Literal[
    # App commands
    "raw_app_command_permissions_update",
    "app_command_completion",
    # AutoMod
    "automod_rule_create",
    "automod_rule_delete",
    "automod_rule_update",
    "automod_action",
    # Channels
    "guild_channel_delete",
    "guild_channel_update",
    "guild_channel_create",
    "guild_channel_pins_update",
    "private_channel_update",
    "private_channel_pins_update",
    "typing",
    "raw_typing",
    # Connection
    "connect",
    "disconnect",
    "shard_connect",
    "shard_disconnect",
    # Debug
    "error",  # This is not a real event
    "socket_event_type",
    "socket_raw_receive",
    "socket_raw_send",
    # Entitlements
    "entitlement_create",
    "entitlement_delete",
    "entitlement_update",
    # Gateway
    "ready",
    "resumed",
    "shard_ready",
    "shard_resumed",
    # Guilds
    "guild_available",
    "guild_unavailable",
    "guild_join",
    "guild_remove",
    "guild_update",
    "guild_emojis_update",
    "guild_stickers_update",
    "audit_log_entry_create",
    "invite_create",
    "invite_delete",
    # Integrations
    "integration_create",
    "integration_update",
    "guild_integrations_update",
    "webhooks_update",
    "raw_integration_delete",
    # Interactions
    "interaction",
    # Members
    "member_join",
    "member_remove",
    "raw_member_remove",
    "member_update",
    "user_update",
    "member_ban",
    "member_unban",
    "presence_update",
    # Messages
    "message",
    "message_edit",
    "message_delete",
    "bulk_message_delete",
    "raw_message_edit",
    "raw_message_delete",
    "raw_bulk_message_delete",
    # Reactions
    "reaction_add",
    "reaction_remove",
    "reaction_clear",
    "reaction_clear_emoji",
    "raw_reaction_add",
    "raw_reaction_remove",
    "raw_reaction_clear",
    "raw_reaction_clear_emoji",
    # Roles
    "guild_role_create",
    "guild_role_delete",
    "guild_role_update",
    # Scheduled Events
    "scheduled_event_create",
    "scheduled_event_update",
    "scheduled_event_delete",
    "scheduled_event_user_add",
    "scheduled_event_user_remove",
    # Stages
    "stage_instance_create",
    "stage_instance_delete",
    "stage_instance_update",
    # Threads
    "thread_create",
    "thread_join",
    "thread_update",
    "thread_remove",
    "thread_delete",
    "raw_thread_update",
    "raw_thread_delete",
    "thread_member_join",
    "thread_member_remove",
    "raw_thread_member_remove",
    # Voice
    "voice_state_update",
]


class Event(Enum):
    # App commands
    RawAppCommandPermissionsUpdate = "raw_app_command_permissions_update"
    AppCommandCompletion = "app_command_completion"
    # AutoMod
    AutoModRuleCreate = "automod_rule_create"
    AutoModRuleDelete = "automod_rule_delete"
    AutoModRuleUpdate = "automod_rule_update"
    AutoModAction = "automod_action"
    # Channels
    GuildChannelDelete = "guild_channel_delete"
    GuildChannelUpdate = "guild_channel_update"
    GuildChannelCreate = "guild_channel_create"
    GuildChannelPinsUpdate = "guild_channel_pins_update"
    PrivateChannelUpdate = "private_channel_update"
    PrivateChannelPinsUpdate = "private_channel_pins_update"
    Typing = "typing"
    RawTyping = "raw_typing"
    # Connection
    Connect = "connect"
    Disconnect = "disconnect"
    ShardConnect = "shard_connect"
    ShardDisconnect = "shard_disconnect"
    # Debug
    Error = "error"  # This is not a real event
    SocketEventType = "socket_event_type"
    SocketRawReceive = "socket_raw_receive"
    SocketRawSend = "socket_raw_send"
    # Entitlements
    EntitlementCreate = "entitlement_create"
    EntitlementDelete = "entitlement_delete"
    EntitlementUpdate = "entitlement_update"
    # Gateway
    Ready = "ready"
    Resumed = "resumed"
    ShardReady = "shard_ready"
    ShardResumed = "shard_resumed"
    # Guilds
    GuildAvailable = "guild_available"
    GuildUnavailable = "guild_unavailable"
    GuildJoin = "guild_join"
    GuildRemove = "guild_remove"
    GuildUpdate = "guild_update"
    GuildEmojisUpdate = "guild_emojis_update"
    GuildStickersUpdate = "guild_stickers_update"
    AuditLogEntryCreate = "audit_log_entry_create"
    InviteCreate = "invite_create"
    InviteDelete = "invite_delete"
    # Integrations
    IntegrationCreate = "integration_create"
    IntegrationUpdate = "integration_update"
    GuildIntegrationsUpdate = "guild_integrations_update"
    WebhooksUpdate = "webhooks_update"
    RawIntergrationDelete = "raw_integration_delete"
    # Interactions
    Interaction = "interaction"
    # Members
    MemberJoin = "member_join"
    MemberRemove = "member_remove"
    RawMemberRemove = "raw_member_remove"
    MemberUpdate = "member_update"
    UserUpdate = "user_update"
    MemberBan = "member_ban"
    MemberUnban = "member_unban"
    PresenceUpdate = "presence_update"
    # Messages
    Message = "message"
    MessageEdit = "message_edit"
    MessageDelete = "message_delete"
    BulkMessageDelete = "bulk_message_delete"
    RawMessageEdit = "raw_message_edit"
    RawMessageDelete = "raw_message_delete"
    RawBulkMessageDelete = "raw_bulk_message_delete"
    # Reactions
    ReactionAdd = "reaction_add"
    ReactionRemove = "reaction_remove"
    ReactionClear = "reaction_clear"
    ReactionClearEmoji = "reaction_clear_emoji"
    RawReactionAdd = "raw_reaction_add"
    RawReactionRemove = "raw_reaction_remove"
    RawReactionClear = "raw_reaction_clear"
    RawReactionClearEmoji = "raw_reaction_clear_emoji"
    # Roles
    GuildRoleCreate = "guild_role_create"
    GuildRoleDelete = "guild_role_delete"
    GuildRoleUpdate = "guild_role_update"
    # Scheduled Events
    ScheduledEventCreate = "scheduled_event_create"
    ScheduledEventUpdate = "scheduled_event_update"
    ScheduledEventDelete = "scheduled_event_delete"
    ScheduledEventUserAdd = "scheduled_event_user_add"
    ScheduledEventUserRemove = "scheduled_event_user_remove"
    # Stages
    StageInstanceCreate = "stage_instance_create"
    StageInstanceDelete = "stage_instance_delete"
    StageInstanceUpdate = "stage_instance_update"
    # Threads
    ThreadCreate = "thread_create"
    ThreadJoin = "thread_join"
    ThreadUpdate = "thread_update"
    ThreadRemove = "thread_remove"
    ThreadDelete = "thread_delete"
    RawThreadUpdate = "raw_thread_update"
    RawThreadDelete = "raw_thread_delete"
    ThreadMemberJoin = "thread_member_join"
    ThreadMemberRemove = "thread_member_remove"
    RawThreadMemberRemove = "raw_thread_member_remove"
    # Voice
    VoiceStateUpdate = "voice_state_update"
