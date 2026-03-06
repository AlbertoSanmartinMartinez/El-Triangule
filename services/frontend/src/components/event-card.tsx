"use client";

import { CalendarDays, MapPin } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import type { Event } from "api-client-typescript";

function formatDate(date?: Date | null): string {
  if (!date) return "";
  return new Intl.DateTimeFormat("es-ES", {
    day: "numeric",
    month: "short",
  }).format(date instanceof Date ? date : new Date(date));
}

export function EventCard({ event }: { event: Event }) {
  return (
    <div className="overflow-hidden rounded-2xl bg-white shadow-sm">
      {/* Gradient header */}
      <div className="relative flex h-36 items-end bg-gradient-to-br from-blue-400 to-primary p-4">
        <Badge variant="accent" className="absolute left-4 top-4 uppercase">
          Evento
        </Badge>
      </div>

      {/* Content */}
      <div className="p-4">
        <h3 className="text-base font-bold text-foreground">{event.title}</h3>

        <div className="mt-2 flex flex-wrap items-center gap-3 text-xs text-muted-foreground">
          {event.date && (
            <span className="flex items-center gap-1">
              <CalendarDays className="h-3.5 w-3.5" />
              {formatDate(event.date)}
            </span>
          )}
          {event.location && (
            <span className="flex items-center gap-1">
              <MapPin className="h-3.5 w-3.5" />
              {event.location}
            </span>
          )}
          {event.price != null && event.price > 0 && (
            <span className="font-semibold text-accent">{event.price}€</span>
          )}
        </div>

        {event.description && (
          <p className="mt-2 line-clamp-2 text-sm text-muted-foreground">
            {event.description}
          </p>
        )}
      </div>
    </div>
  );
}
