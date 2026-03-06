import {
  Configuration,
  UserApi,
  EventApi,
  NotificationApi,
  AlbumApi,
  ImageApi,
  ConversationApi,
  MessageApi,
  PaymentApi,
  type Middleware,
} from "api-client-typescript";
import { getAccessToken } from "./auth";

const authMiddleware: Middleware = {
  async pre(context) {
    const token = getAccessToken();
    if (token) {
      return {
        url: context.url,
        init: {
          ...context.init,
          headers: {
            ...context.init.headers,
            Authorization: `Bearer ${token}`,
          },
        },
      };
    }
    return context;
  },
};

const config = new Configuration({
  basePath: process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000",
  middleware: [authMiddleware],
});

export const userApi = new UserApi(config);
export const eventApi = new EventApi(config);
export const notificationApi = new NotificationApi(config);
export const albumApi = new AlbumApi(config);
export const imageApi = new ImageApi(config);
export const conversationApi = new ConversationApi(config);
export const messageApi = new MessageApi(config);
export const paymentApi = new PaymentApi(config);
