"use client";

import { ImageIcon } from "lucide-react";

export default function GalleryPage() {
  return (
    <div className="flex flex-col items-center justify-center px-6 pt-24">
      <div className="flex h-20 w-20 items-center justify-center rounded-full bg-primary/10">
        <ImageIcon className="h-10 w-10 text-primary" />
      </div>
      <h1 className="mt-6 text-2xl font-black text-foreground">GALERÍA</h1>
      <p className="mt-2 text-center text-sm text-muted-foreground">
        Próximamente podrás ver las fotos y álbumes aquí.
      </p>
    </div>
  );
}
