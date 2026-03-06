"use client";

import { CalendarDays } from "lucide-react";

export default function AgendaPage() {
  return (
    <div className="flex flex-col items-center justify-center px-6 pt-24">
      <div className="flex h-20 w-20 items-center justify-center rounded-full bg-primary/10">
        <CalendarDays className="h-10 w-10 text-primary" />
      </div>
      <h1 className="mt-6 text-2xl font-black text-foreground">AGENDA</h1>
      <p className="mt-2 text-center text-sm text-muted-foreground">
        Próximamente podrás ver el calendario de eventos aquí.
      </p>
    </div>
  );
}
