"use client";

import {
  createContext,
  useContext,
  useState,
  useEffect,
  useCallback,
  type ReactNode,
} from "react";
import { useRouter } from "next/navigation";
import {
  getUserFromToken,
  setTokens,
  clearTokens,
  isAuthenticated as checkAuth,
} from "./auth";
import { userApi } from "./api";

interface AuthUser {
  uuid: string;
  role: string;
}

interface AuthContextValue {
  user: AuthUser | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  login: (email: string, password: string) => Promise<void>;
  register: (email: string, password: string) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextValue | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const router = useRouter();
  const [user, setUser] = useState<AuthUser | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const u = getUserFromToken();
    setUser(u);
    setIsLoading(false);
  }, []);

  const login = useCallback(
    async (email: string, password: string) => {
      const response = await userApi.loginApiAuthUserLoginPost({
        loginRequest: { email, password },
      });
      setTokens(response.accessToken, response.refreshToken);
      setUser(getUserFromToken());
      router.push("/");
    },
    [router]
  );

  const register = useCallback(
    async (email: string, password: string) => {
      const response = await userApi.registerApiAuthUserRegisterPost({
        registerRequest: { email, password },
      });
      setTokens(response.accessToken, response.refreshToken);
      setUser(getUserFromToken());
      router.push("/");
    },
    [router]
  );

  const logout = useCallback(() => {
    clearTokens();
    setUser(null);
    router.push("/login");
  }, [router]);

  return (
    <AuthContext.Provider
      value={{
        user,
        isAuthenticated: checkAuth(),
        isLoading,
        login,
        register,
        logout,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within AuthProvider");
  }
  return context;
}
