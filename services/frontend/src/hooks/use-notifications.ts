"use client";

import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { notificationApi } from "@/lib/api";

export function useNotifications(filters?: Record<string, unknown>) {
  return useQuery({
    queryKey: ["notifications", filters],
    queryFn: () =>
      notificationApi.listApiNotificationsNotificationGet({
        filters: filters as never,
      }),
  });
}

export function useUnreadCount() {
  return useQuery({
    queryKey: ["notifications", "unread-count"],
    queryFn: () => notificationApi.unreadCountApiNotificationsNotificationUnreadCountGet(),
    refetchInterval: 30_000,
  });
}

export function useMarkRead() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: (uuid: string) =>
      notificationApi.markReadApiNotificationsNotificationUuidReadPatch({ uuid }),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ["notifications"] });
    },
  });
}

export function useMarkAllRead() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: () =>
      notificationApi.markAllReadApiNotificationsNotificationReadAllPatch(),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ["notifications"] });
    },
  });
}
