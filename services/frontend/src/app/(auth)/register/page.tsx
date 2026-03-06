"use client";

import { useState } from "react";
import Link from "next/link";
import { ArrowLeft, User, CalendarDays, Mail, Phone, Lock, Camera } from "lucide-react";
import { useAuth } from "@/lib/auth-provider";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { cn } from "@/lib/utils";

const TOTAL_STEPS = 3;

export default function RegisterPage() {
  const { register } = useAuth();
  const [step, setStep] = useState(1);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const [name, setName] = useState("");
  const [birthDate, setBirthDate] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  function nextStep() {
    setError("");
    if (step === 1) {
      if (!name || !email) {
        setError("Nombre y email son obligatorios");
        return;
      }
    }
    if (step === 2) {
      if (!password || password.length < 6) {
        setError("La contraseña debe tener al menos 6 caracteres");
        return;
      }
      if (password !== confirmPassword) {
        setError("Las contraseñas no coinciden");
        return;
      }
    }
    setStep((s) => Math.min(s + 1, TOTAL_STEPS));
  }

  function prevStep() {
    setError("");
    setStep((s) => Math.max(s - 1, 1));
  }

  async function handleSubmit() {
    setError("");
    setLoading(true);
    try {
      await register(email, password);
    } catch {
      setError("Error al crear la cuenta. Inténtalo de nuevo.");
    } finally {
      setLoading(false);
    }
  }

  const stepLabels = ["Datos personales", "Contraseña", "Confirmación"];

  return (
    <div className="flex min-h-dvh flex-col">
      {/* Header */}
      <div className="bg-accent px-6 pb-10 pt-12">
        <Link href="/login" className="mb-4 inline-flex h-10 w-10 items-center justify-center rounded-full bg-white/20">
          <ArrowLeft className="h-5 w-5 text-white" />
        </Link>
        <h1 className="text-3xl font-black italic text-white">
          ÚNETE A<br />LA PEÑA
        </h1>
        <p className="mt-2 text-sm text-white/80">
          Paso {step} de {TOTAL_STEPS} — {stepLabels[step - 1]}
        </p>
      </div>

      {/* Progress bar */}
      <div className="flex gap-2 bg-white px-6 pt-6">
        {Array.from({ length: TOTAL_STEPS }).map((_, i) => (
          <div
            key={i}
            className={cn(
              "h-1.5 flex-1 rounded-full transition-colors",
              i < step ? "bg-accent" : i === step - 1 ? "bg-primary" : "bg-gray-200"
            )}
          />
        ))}
      </div>

      {/* Form */}
      <div className="flex-1 bg-white px-6 pb-8 pt-6">
        {step === 1 && (
          <div className="space-y-4">
            <div className="mb-6 flex items-center gap-4">
              <div className="flex h-16 w-16 items-center justify-center rounded-full bg-gray-100">
                <User className="h-8 w-8 text-gray-400" />
              </div>
              <button
                type="button"
                className="flex items-center gap-2 rounded-full border border-gray-200 px-4 py-2 text-sm text-muted-foreground"
              >
                <Camera className="h-4 w-4" />
                Añadir foto
              </button>
            </div>

            <p className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
              Información personal
            </p>

            <div className="relative">
              <User className="absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2 text-muted-foreground" />
              <Input
                placeholder="Nombre completo"
                value={name}
                onChange={(e) => setName(e.target.value)}
                className="pl-12"
              />
            </div>

            <div className="relative">
              <CalendarDays className="absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2 text-muted-foreground" />
              <Input
                type="date"
                placeholder="Fecha de nacimiento"
                value={birthDate}
                onChange={(e) => setBirthDate(e.target.value)}
                className="pl-12"
              />
            </div>

            <div className="relative">
              <Mail className="absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2 text-muted-foreground" />
              <Input
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="pl-12"
                required
              />
            </div>

            <div className="relative">
              <Phone className="absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2 text-muted-foreground" />
              <Input
                type="tel"
                placeholder="Teléfono"
                value={phone}
                onChange={(e) => setPhone(e.target.value)}
                className="pl-12"
              />
            </div>
          </div>
        )}

        {step === 2 && (
          <div className="space-y-4">
            <p className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
              Crea tu contraseña
            </p>

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

            <div className="relative">
              <Lock className="absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2 text-muted-foreground" />
              <Input
                type="password"
                placeholder="Confirmar contraseña"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                className="pl-12"
                required
              />
            </div>
          </div>
        )}

        {step === 3 && (
          <div className="space-y-4 text-center">
            <div className="mx-auto flex h-20 w-20 items-center justify-center rounded-full bg-accent/10">
              <User className="h-10 w-10 text-accent" />
            </div>
            <h3 className="text-lg font-bold">¡Todo listo!</h3>
            <p className="text-sm text-muted-foreground">
              Revisa tus datos antes de crear tu cuenta.
            </p>
            <div className="rounded-xl bg-gray-50 p-4 text-left text-sm">
              <p><span className="font-medium">Nombre:</span> {name || "—"}</p>
              <p><span className="font-medium">Email:</span> {email}</p>
              <p><span className="font-medium">Teléfono:</span> {phone || "—"}</p>
              <p><span className="font-medium">Nacimiento:</span> {birthDate || "—"}</p>
            </div>
          </div>
        )}

        {error && (
          <p className="mt-4 text-center text-sm text-destructive">{error}</p>
        )}

        <div className="mt-8 flex gap-3">
          {step > 1 && (
            <Button variant="outline" onClick={prevStep} className="flex-1">
              Atrás
            </Button>
          )}
          {step < TOTAL_STEPS ? (
            <Button onClick={nextStep} className="flex-1">
              Siguiente
            </Button>
          ) : (
            <Button
              onClick={handleSubmit}
              variant="accent"
              className="flex-1"
              disabled={loading}
            >
              {loading ? "Creando cuenta..." : "CREAR CUENTA"}
            </Button>
          )}
        </div>

        {step === 1 && (
          <div className="mt-6 text-center text-sm text-muted-foreground">
            ¿Ya tienes cuenta?{" "}
            <Link href="/login" className="font-semibold text-primary hover:underline">
              Inicia sesión
            </Link>
          </div>
        )}
      </div>
    </div>
  );
}
