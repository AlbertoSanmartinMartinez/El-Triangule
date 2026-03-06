"use client";

import { Bell, MessageCircle, CalendarDays, ImageIcon, CreditCard, UserPlus } from "lucide-react";
import { cn } from "@/lib/utils";
import type { Notification } from "api-client-typescript";

const TYPE_ICONS: Record<string, typeof Bell> = {
  event: CalendarDays,
  message: MessageCircle,
  image: ImageIcon,
  payment: CreditCard,
  member: UserPlus,
};

function timeAgo(date?: Date | null): string {
  if (!date) return "";
  const now = Date.now();
  const d = date instanceof Date ? date : new Date(date);
  const diff = now - d.getTime();
  const minutes = Math.floor(diff / 60_000);
  if (minutes < 1) return "Ahora";
  if (minutes < 60) return `Hace ${minutes} min`;
  const hours = Math.floor(minutes / 60);
  if (hours < 24) return `Hace ${hours}h`;
  const days = Math.floor(hours / 24);
  if (days === 1) return "Ayer";
  return `Hace ${days} días`;
}

export function NotificationItem({
  notification,
  onMarkRead,
}: {
  notification: Notification;
  onMarkRead?: (uuid: string) => void;
}) {
  const Icon = TYPE_ICONS[notification.notificationType] ?? Bell;
  const isUnread = !notification.isRead;

  return (
    <button
      onClick={() => {
        if (isUnread && notification.uuid && onMarkRead) {
          onMarkRead(notification.uuid);
        }
      }}
      className={cn(
        "flex w-full items-start gap-3 rounded-xl p-3 text-left transition-colors",
        isUnread ? "bg-white" : "bg-gray-50/50"
      )}
    >
      {/* Unread indicator */}
      <div
        className={cn(
          "mt-1 w-1 shrink-0 self-stretch rounded-full",
          isUnread ? "bg-accent" : "bg-transparent"
        )}
      />

      {/* Icon */}
      <div
        className={cn(
          "flex h-10 w-10 shrink-0 items-center justify-center rounded-full",
          isUnread ? "bg-accent/10 text-accent" : "bg-gray-100 text-gray-400"
        )}
      >
        <Icon className="h-5 w-5" />
      </div>

      {/* Content */}
      <div className="min-w-0 flex-1">
        <p className={cn("text-sm", isUnread ? "font-semibold text-foreground" : "text-muted-foreground")}>
          {notification.title}
        </p>
        <p className="mt-0.5 line-clamp-2 text-xs text-muted-foreground">
          {notification.body}
        </p>
        <p className="mt-1 text-[11px] text-gray-400">
          {timeAgo(notification.createdAt)}
        </p>
      </div>
    </button>
  );
}
