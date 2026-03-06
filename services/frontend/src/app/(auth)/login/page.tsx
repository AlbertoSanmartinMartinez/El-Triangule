"use client";

import { useState } from "react";
import Link from "next/link";
import { Lock, Mail } from "lucide-react";
import { useAuth } from "@/lib/auth-provider";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

export default function LoginPage() {
  const { login } = useAuth();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      await login(email, password);
    } catch {
      setError("Email o contraseña incorrectos");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="flex min-h-dvh flex-col">
      {/* Header */}
      <div className="flex flex-1 flex-col items-center justify-center bg-primary px-6 pb-12 pt-16">
        <div className="mb-4 flex h-20 w-20 items-center justify-center rounded-2xl bg-accent text-2xl font-black text-white shadow-lg">
          PJ
        </div>
        <h1 className="text-2xl font-black tracking-wider text-white">
          PEÑA JOVEN
        </h1>
        <p className="mt-1 text-sm text-white/60">La peña del pueblo</p>
      </div>

      {/* Form card */}
      <div className="-mt-8 flex-1 rounded-t-3xl bg-white px-6 pb-8 pt-8 shadow-xl">
        <h2 className="mb-6 text-center text-2xl font-black text-foreground">
          BIENVENIDO
        </h2>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="relative">
            <Mail className="absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2 text-muted-foreground" />
            <Input
              type="email"
              placeholder="correo@email.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="pl-12"
              required
            />
          </div>

          <div className="relative">
            <Lock className="absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2 text-muted-foreground" />
            <Input
              type="password"
              placeholder="Contraseña"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="pl-12"
              required
            />
          </div>

          <div className="text-center">
            <Link
              href="#"
              className="text-sm text-primary hover:underline"
            >
              ¿Olvidaste tu contraseña?
            </Link>
          </div>

          {error && (
            <p className="text-center text-sm text-destructive">{error}</p>
          )}

          <Button
            type="submit"
            className="w-full"
            disabled={loading}
          >
            {loading ? "Entrando..." : "ENTRAR"}
          </Button>
        </form>

        <div className="mt-6 text-center text-sm text-muted-foreground">
          ¿No tienes cuenta?{" "}
          <Link href="/register" className="font-semibold text-primary hover:underline">
            Únete a la peña
          </Link>
        </div>
      </div>
    </div>
  );
}
