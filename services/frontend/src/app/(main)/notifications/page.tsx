"use client";

import { ArrowLeft } from "lucide-react";
import Link from "next/link";
import { useNotifications, useMarkRead, useMarkAllRead } from "@/hooks/use-notifications";
import { NotificationItem } from "@/components/notification-item";

export default function NotificationsPage() {
  const { data, isLoading } = useNotifications();
  const markRead = useMarkRead();
  const markAllRead = useMarkAllRead();

  const notifications = data?.items ?? [];
  const unread = notifications.filter((n) => !n.isRead);
  const read = notifications.filter((n) => n.isRead);

  return (
    <div className="flex flex-col">
      {/* Header */}
      <div className="flex items-center justify-between bg-white px-6 pb-4 pt-12">
        <div className="flex items-center gap-3">
          <Link href="/" className="text-foreground">
            <ArrowLeft className="h-5 w-5" />
          </Link>
          <h1 className="text-2xl font-black text-foreground">AVISOS</h1>
        </div>
        <button
          onClick={() => markAllRead.mutate()}
          className="text-sm font-medium text-primary hover:underline"
          disabled={markAllRead.isPending}
        >
          Marcar todo leído
        </button>
      </div>

      {isLoading ? (
        <div className="space-y-3 px-6 pt-4">
          {[1, 2, 3, 4].map((i) => (
            <div key={i} className="h-20 animate-pulse rounded-xl bg-gray-200" />
          ))}
        </div>
      ) : notifications.length === 0 ? (
        <div className="px-6 py-16 text-center text-sm text-muted-foreground">
          No tienes notificaciones
        </div>
      ) : (
        <div className="px-6">
          {/* Unread */}
          {unread.length > 0 && (
            <div className="mt-4">
              <p className="mb-2 text-xs font-semibold uppercase tracking-wider text-muted-foreground">
                Nuevas
              </p>
              <div className="space-y-2">
                {unread.map((n) => (
                  <NotificationItem
                    key={n.uuid}
                    notification={n}
                    onMarkRead={(uuid) => markRead.mutate(uuid)}
                  />
                ))}
              </div>
            </div>
          )}

          {/* Read */}
          {read.length > 0 && (
            <div className="mt-6">
              <p className="mb-2 text-xs font-semibold uppercase tracking-wider text-muted-foreground">
                Anteriores
              </p>
              <div className="space-y-2">
                {read.map((n) => (
                  <NotificationItem key={n.uuid} notification={n} />
                ))}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
