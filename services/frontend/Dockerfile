FROM node:22-alpine AS base
RUN corepack enable && corepack prepare pnpm@latest --activate

FROM base AS deps
WORKDIR /app
COPY packages/api-client-typescript /packages/api-client-typescript
COPY services/frontend/package.json services/frontend/pnpm-lock.yaml ./
RUN pnpm install --no-frozen-lockfile

FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY --from=deps /packages/api-client-typescript /packages/api-client-typescript
COPY services/frontend/ .
RUN pnpm build

FROM base AS runner
RUN apk add --no-cache curl
WORKDIR /app
ENV NODE_ENV=production

COPY --from=builder /app/public ./public
COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/static ./.next/static

EXPOSE 3000
ENV HOSTNAME="0.0.0.0"
CMD ["node", "server.js"]
