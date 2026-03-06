"use client";

import { useState } from "react";
import Link from "next/link";
import { Bell, Search } from "lucide-react";
import { useAuth } from "@/lib/auth-provider";
import { useEvents } from "@/hooks/use-events";
import { useUnreadCount } from "@/hooks/use-notifications";
import { Tabs } from "@/components/ui/tabs";
import { Input } from "@/components/ui/input";
import { EventCard } from "@/components/event-card";

const FEED_TABS = ["Todo", "Eventos", "Noticias", "Fotos"];

export default function HomePage() {
  const { user } = useAuth();
  const [activeTab, setActiveTab] = useState("Todo");
  const [search, setSearch] = useState("");

  const { data: eventsData, isLoading } = useEvents();
  const { data: unreadData } = useUnreadCount();

  const events = eventsData?.items ?? [];
  const unreadCount = (unreadData as { count?: number })?.count ?? 0;

  return (
    <div className="flex flex-col">
      {/* Header */}
      <div className="bg-primary px-6 pb-6 pt-12">
        <div className="flex items-start justify-between">
          <div>
            <p className="text-sm text-white/70">¡Buenos días!</p>
            <h1 className="text-2xl font-black text-white">
              HOLA{user ? `, ${user.uuid.slice(0, 6).toUpperCase()}` : ""}
            </h1>
          </div>
          <Link href="/notifications" className="relative mt-1">
            <Bell className="h-7 w-7 text-accent" fill="currentColor" />
            {unreadCount > 0 && (
              <span className="absolute -right-1.5 -top-1.5 flex h-5 w-5 items-center justify-center rounded-full bg-destructive text-[10px] font-bold text-white">
                {unreadCount > 9 ? "9+" : unreadCount}
              </span>
            )}
          </Link>
        </div>
      </div>

      {/* Search */}
      <div className="px-6 -mt-4">
        <div className="relative">
          <Search className="absolute left-4 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
          <Input
            placeholder="Buscar noticias..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="bg-white pl-11 shadow-sm"
          />
        </div>
      </div>

      {/* Tabs */}
      <div className="px-6 pt-4">
        <Tabs tabs={FEED_TABS} active={activeTab} onChange={setActiveTab} />
      </div>

      {/* Feed */}
      <div className="space-y-4 px-6 pt-4">
        {isLoading ? (
          <div className="space-y-4">
            {[1, 2, 3].map((i) => (
              <div
                key={i}
                className="h-52 animate-pulse rounded-2xl bg-gray-200"
              />
            ))}
          </div>
        ) : events.length === 0 ? (
          <div className="py-12 text-center text-sm text-muted-foreground">
            No hay eventos disponibles
          </div>
        ) : (
          events.map((event) => (
            <EventCard key={event.uuid} event={event} />
          ))
        )}
      </div>
    </div>
  );
}
