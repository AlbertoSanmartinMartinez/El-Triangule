"use client";

import { MessageCircle } from "lucide-react";

export default function ChatPage() {
  return (
    <div className="flex flex-col items-center justify-center px-6 pt-24">
      <div className="flex h-20 w-20 items-center justify-center rounded-full bg-primary/10">
        <MessageCircle className="h-10 w-10 text-primary" />
      </div>
      <h1 className="mt-6 text-2xl font-black text-foreground">MENSAJES</h1>
      <p className="mt-2 text-center text-sm text-muted-foreground">
        Próximamente podrás chatear con los miembros aquí.
      </p>
    </div>
  );
}
