"use client";

import { useQuery } from "@tanstack/react-query";
import { eventApi } from "@/lib/api";

export function useEvents(filters?: Record<string, unknown>) {
  return useQuery({
    queryKey: ["events", filters],
    queryFn: () => eventApi.listApiEventsEventGet({ filters: filters as never }),
  });
}
