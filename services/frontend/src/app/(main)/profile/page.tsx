"use client";

import { UserIcon, LogOut, Settings, Bell, Shield } from "lucide-react";
import { useAuth } from "@/lib/auth-provider";
import { Button } from "@/components/ui/button";

export default function ProfilePage() {
  const { user, logout } = useAuth();

  return (
    <div className="flex flex-col">
      {/* Header */}
      <div className="flex flex-col items-center bg-primary px-6 pb-8 pt-16">
        <div className="flex h-24 w-24 items-center justify-center rounded-full bg-accent text-3xl">
          😊
        </div>
        <h1 className="mt-4 text-xl font-black text-white">
          {user?.uuid.slice(0, 8).toUpperCase() ?? "USUARIO"}
        </h1>
        <p className="mt-1 text-sm text-white/60">
          Miembro · {user?.role ?? "user"}
        </p>
      </div>

      {/* Menu */}
      <div className="space-y-2 px-6 pt-6">
        <p className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
          Cuenta
        </p>

        <MenuItem icon={UserIcon} label="Editar perfil" />
        <MenuItem icon={Shield} label="Privacidad y seguridad" />

        <p className="mt-4 text-xs font-semibold uppercase tracking-wider text-muted-foreground">
          Preferencias
        </p>

        <MenuItem icon={Bell} label="Notificaciones" />
        <MenuItem icon={Settings} label="Configuración" />
      </div>

      <div className="px-6 pt-8">
        <Button variant="outline" className="w-full text-destructive" onClick={logout}>
          <LogOut className="h-4 w-4" />
          Cerrar sesión
        </Button>
      </div>
    </div>
  );
}

function MenuItem({ icon: Icon, label }: { icon: typeof UserIcon; label: string }) {
  return (
    <button className="flex w-full items-center gap-4 rounded-xl bg-white p-4 text-left shadow-sm transition-colors hover:bg-gray-50">
      <div className="flex h-10 w-10 items-center justify-center rounded-full bg-gray-100">
        <Icon className="h-5 w-5 text-muted-foreground" />
      </div>
      <span className="flex-1 text-sm font-medium text-foreground">{label}</span>
      <span className="text-gray-300">›</span>
    </button>
  );
}
