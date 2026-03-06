const ACCESS_TOKEN_KEY = "eltriangule_access_token";
const REFRESH_TOKEN_KEY = "eltriangule_refresh_token";

export function getAccessToken(): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem(ACCESS_TOKEN_KEY);
}

export function getRefreshToken(): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem(REFRESH_TOKEN_KEY);
}

export function setTokens(accessToken: string, refreshToken: string) {
  localStorage.setItem(ACCESS_TOKEN_KEY, accessToken);
  localStorage.setItem(REFRESH_TOKEN_KEY, refreshToken);
  document.cookie = `${ACCESS_TOKEN_KEY}=${accessToken}; path=/; SameSite=Lax`;
}

export function clearTokens() {
  localStorage.removeItem(ACCESS_TOKEN_KEY);
  localStorage.removeItem(REFRESH_TOKEN_KEY);
  document.cookie = `${ACCESS_TOKEN_KEY}=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT`;
}

export function isAuthenticated(): boolean {
  return !!getAccessToken();
}

interface JwtPayload {
  sub: string;
  role: string;
  exp: number;
  type: string;
}

export function getUserFromToken(): { uuid: string; role: string } | null {
  const token = getAccessToken();
  if (!token) return null;
  try {
    const payload: JwtPayload = JSON.parse(atob(token.split(".")[1]));
    if (payload.exp * 1000 < Date.now()) {
      clearTokens();
      return null;
    }
    return { uuid: payload.sub, role: payload.role };
  } catch {
    return null;
  }
}
