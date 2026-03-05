# api-client-typescript@1.0.0

A TypeScript SDK client for the localhost API.

## Usage

First, install the SDK from npm.

```bash
npm install api-client-typescript --save
```

Next, try it out.


```ts
import {
  Configuration,
  AlbumApi,
} from 'api-client-typescript';
import type { CreateApiImagesAlbumPostRequest } from 'api-client-typescript';

async function example() {
  console.log("🚀 Testing api-client-typescript SDK...");
  const api = new AlbumApi();

  const body = {
    // Album
    album: ...,
  } satisfies CreateApiImagesAlbumPostRequest;

  try {
    const data = await api.createApiImagesAlbumPost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```


## Documentation

### API Endpoints

All URIs are relative to *http://localhost*

| Class | Method | HTTP request | Description
| ----- | ------ | ------------ | -------------
*AlbumApi* | [**createApiImagesAlbumPost**](docs/AlbumApi.md#createapiimagesalbumpost) | **POST** /api/images/album | Create
*AlbumApi* | [**deleteApiImagesAlbumPkDelete**](docs/AlbumApi.md#deleteapiimagesalbumpkdelete) | **DELETE** /api/images/album/{pk} | Delete
*AlbumApi* | [**detailApiImagesAlbumPkGet**](docs/AlbumApi.md#detailapiimagesalbumpkget) | **GET** /api/images/album/{pk} | Detail
*AlbumApi* | [**listApiImagesAlbumGet**](docs/AlbumApi.md#listapiimagesalbumget) | **GET** /api/images/album | List
*AlbumApi* | [**updateApiImagesAlbumPkPatch**](docs/AlbumApi.md#updateapiimagesalbumpkpatch) | **PATCH** /api/images/album/{pk} | Update
*ConversationApi* | [**addMemberApiMessagesConversationUuidMemberPost**](docs/ConversationApi.md#addmemberapimessagesconversationuuidmemberpost) | **POST** /api/messages/conversation/{uuid}/member | Add member to conversation
*ConversationApi* | [**createApiMessagesConversationPost**](docs/ConversationApi.md#createapimessagesconversationpost) | **POST** /api/messages/conversation | Create
*ConversationApi* | [**deleteApiMessagesConversationPkDelete**](docs/ConversationApi.md#deleteapimessagesconversationpkdelete) | **DELETE** /api/messages/conversation/{pk} | Delete
*ConversationApi* | [**detailApiMessagesConversationPkGet**](docs/ConversationApi.md#detailapimessagesconversationpkget) | **GET** /api/messages/conversation/{pk} | Detail
*ConversationApi* | [**listApiMessagesConversationGet**](docs/ConversationApi.md#listapimessagesconversationget) | **GET** /api/messages/conversation | List
*ConversationApi* | [**removeMemberApiMessagesConversationUuidMemberUserUuidDelete**](docs/ConversationApi.md#removememberapimessagesconversationuuidmemberuseruuiddelete) | **DELETE** /api/messages/conversation/{uuid}/member/{user_uuid} | Remove member from conversation
*ConversationApi* | [**updateApiMessagesConversationPkPatch**](docs/ConversationApi.md#updateapimessagesconversationpkpatch) | **PATCH** /api/messages/conversation/{pk} | Update
*DefaultApi* | [**healthCheckApiHealthGet**](docs/DefaultApi.md#healthcheckapihealthget) | **GET** /api/health | Health Check
*EventApi* | [**createApiEventsEventPost**](docs/EventApi.md#createapieventseventpost) | **POST** /api/events/event | Create
*EventApi* | [**deleteApiEventsEventPkDelete**](docs/EventApi.md#deleteapieventseventpkdelete) | **DELETE** /api/events/event/{pk} | Delete
*EventApi* | [**detailApiEventsEventPkGet**](docs/EventApi.md#detailapieventseventpkget) | **GET** /api/events/event/{pk} | Detail
*EventApi* | [**listApiEventsEventGet**](docs/EventApi.md#listapieventseventget) | **GET** /api/events/event | List
*EventApi* | [**registerEventApiEventsEventUuidRegisterPost**](docs/EventApi.md#registereventapieventseventuuidregisterpost) | **POST** /api/events/event/{uuid}/register | Register to event
*EventApi* | [**unregisterEventApiEventsEventUuidRegisterDelete**](docs/EventApi.md#unregistereventapieventseventuuidregisterdelete) | **DELETE** /api/events/event/{uuid}/register | Unregister from event
*EventApi* | [**updateApiEventsEventPkPatch**](docs/EventApi.md#updateapieventseventpkpatch) | **PATCH** /api/events/event/{pk} | Update
*ImageApi* | [**createApiImagesImagePost**](docs/ImageApi.md#createapiimagesimagepost) | **POST** /api/images/image | Create
*ImageApi* | [**deleteApiImagesImagePkDelete**](docs/ImageApi.md#deleteapiimagesimagepkdelete) | **DELETE** /api/images/image/{pk} | Delete
*ImageApi* | [**detailApiImagesImagePkGet**](docs/ImageApi.md#detailapiimagesimagepkget) | **GET** /api/images/image/{pk} | Detail
*ImageApi* | [**listApiImagesImageGet**](docs/ImageApi.md#listapiimagesimageget) | **GET** /api/images/image | List
*ImageApi* | [**updateApiImagesImagePkPatch**](docs/ImageApi.md#updateapiimagesimagepkpatch) | **PATCH** /api/images/image/{pk} | Update
*MessageApi* | [**createApiMessagesMessagePost**](docs/MessageApi.md#createapimessagesmessagepost) | **POST** /api/messages/message | Create
*MessageApi* | [**deleteApiMessagesMessagePkDelete**](docs/MessageApi.md#deleteapimessagesmessagepkdelete) | **DELETE** /api/messages/message/{pk} | Delete
*MessageApi* | [**detailApiMessagesMessagePkGet**](docs/MessageApi.md#detailapimessagesmessagepkget) | **GET** /api/messages/message/{pk} | Detail
*MessageApi* | [**listApiMessagesMessageGet**](docs/MessageApi.md#listapimessagesmessageget) | **GET** /api/messages/message | List
*MessageApi* | [**updateApiMessagesMessagePkPatch**](docs/MessageApi.md#updateapimessagesmessagepkpatch) | **PATCH** /api/messages/message/{pk} | Update
*NotificationApi* | [**createApiNotificationsNotificationPost**](docs/NotificationApi.md#createapinotificationsnotificationpost) | **POST** /api/notifications/notification | Create
*NotificationApi* | [**deleteApiNotificationsNotificationPkDelete**](docs/NotificationApi.md#deleteapinotificationsnotificationpkdelete) | **DELETE** /api/notifications/notification/{pk} | Delete
*NotificationApi* | [**detailApiNotificationsNotificationPkGet**](docs/NotificationApi.md#detailapinotificationsnotificationpkget) | **GET** /api/notifications/notification/{pk} | Detail
*NotificationApi* | [**listApiNotificationsNotificationGet**](docs/NotificationApi.md#listapinotificationsnotificationget) | **GET** /api/notifications/notification | List
*NotificationApi* | [**markAllReadApiNotificationsNotificationReadAllPatch**](docs/NotificationApi.md#markallreadapinotificationsnotificationreadallpatch) | **PATCH** /api/notifications/notification/read-all | Mark all notifications as read
*NotificationApi* | [**markReadApiNotificationsNotificationUuidReadPatch**](docs/NotificationApi.md#markreadapinotificationsnotificationuuidreadpatch) | **PATCH** /api/notifications/notification/{uuid}/read | Mark notification as read
*NotificationApi* | [**unreadCountApiNotificationsNotificationUnreadCountGet**](docs/NotificationApi.md#unreadcountapinotificationsnotificationunreadcountget) | **GET** /api/notifications/notification/unread-count | Unread notifications count
*NotificationApi* | [**updateApiNotificationsNotificationPkPatch**](docs/NotificationApi.md#updateapinotificationsnotificationpkpatch) | **PATCH** /api/notifications/notification/{pk} | Update
*PaymentApi* | [**createApiPaymentsPaymentPost**](docs/PaymentApi.md#createapipaymentspaymentpost) | **POST** /api/payments/payment | Create
*PaymentApi* | [**deleteApiPaymentsPaymentPkDelete**](docs/PaymentApi.md#deleteapipaymentspaymentpkdelete) | **DELETE** /api/payments/payment/{pk} | Delete
*PaymentApi* | [**detailApiPaymentsPaymentPkGet**](docs/PaymentApi.md#detailapipaymentspaymentpkget) | **GET** /api/payments/payment/{pk} | Detail
*PaymentApi* | [**listApiPaymentsPaymentGet**](docs/PaymentApi.md#listapipaymentspaymentget) | **GET** /api/payments/payment | List
*PaymentApi* | [**refundPaymentApiPaymentsPaymentUuidRefundPost**](docs/PaymentApi.md#refundpaymentapipaymentspaymentuuidrefundpost) | **POST** /api/payments/payment/{uuid}/refund | Refund payment
*PaymentApi* | [**updateApiPaymentsPaymentPkPatch**](docs/PaymentApi.md#updateapipaymentspaymentpkpatch) | **PATCH** /api/payments/payment/{pk} | Update
*UserApi* | [**createApiAuthUserPost**](docs/UserApi.md#createapiauthuserpost) | **POST** /api/auth/user | Create
*UserApi* | [**deleteApiAuthUserPkDelete**](docs/UserApi.md#deleteapiauthuserpkdelete) | **DELETE** /api/auth/user/{pk} | Delete
*UserApi* | [**detailApiAuthUserPkGet**](docs/UserApi.md#detailapiauthuserpkget) | **GET** /api/auth/user/{pk} | Detail
*UserApi* | [**listApiAuthUserGet**](docs/UserApi.md#listapiauthuserget) | **GET** /api/auth/user | List
*UserApi* | [**loginApiAuthUserLoginPost**](docs/UserApi.md#loginapiauthuserloginpost) | **POST** /api/auth/user/login | User login
*UserApi* | [**refreshApiAuthUserRefreshPost**](docs/UserApi.md#refreshapiauthuserrefreshpost) | **POST** /api/auth/user/refresh | Refresh token
*UserApi* | [**registerApiAuthUserRegisterPost**](docs/UserApi.md#registerapiauthuserregisterpost) | **POST** /api/auth/user/register | User register
*UserApi* | [**updateApiAuthUserPkPatch**](docs/UserApi.md#updateapiauthuserpkpatch) | **PATCH** /api/auth/user/{pk} | Update


### Models

- [AddMemberRequest](docs/AddMemberRequest.md)
- [Album](docs/Album.md)
- [Conversation](docs/Conversation.md)
- [ConversationMember](docs/ConversationMember.md)
- [ConversationType](docs/ConversationType.md)
- [Event](docs/Event.md)
- [FiltersInterface](docs/FiltersInterface.md)
- [HTTPValidationError](docs/HTTPValidationError.md)
- [Image](docs/Image.md)
- [ListResponseAlbum](docs/ListResponseAlbum.md)
- [ListResponseConversation](docs/ListResponseConversation.md)
- [ListResponseEvent](docs/ListResponseEvent.md)
- [ListResponseImage](docs/ListResponseImage.md)
- [ListResponseMessage](docs/ListResponseMessage.md)
- [ListResponseNotification](docs/ListResponseNotification.md)
- [ListResponsePayment](docs/ListResponsePayment.md)
- [ListResponseUser](docs/ListResponseUser.md)
- [LocationInner](docs/LocationInner.md)
- [LoginRequest](docs/LoginRequest.md)
- [MemberRole](docs/MemberRole.md)
- [Message](docs/Message.md)
- [Notification](docs/Notification.md)
- [OrderDirection](docs/OrderDirection.md)
- [OrderParams](docs/OrderParams.md)
- [OrderParams1](docs/OrderParams1.md)
- [PaginationParams](docs/PaginationParams.md)
- [PaginationParams1](docs/PaginationParams1.md)
- [Payment](docs/Payment.md)
- [RefreshRequest](docs/RefreshRequest.md)
- [RegisterRequest](docs/RegisterRequest.md)
- [Role](docs/Role.md)
- [SearchParams](docs/SearchParams.md)
- [TokenResponse](docs/TokenResponse.md)
- [User](docs/User.md)
- [ValidationError](docs/ValidationError.md)

### Authorization

Endpoints do not require authorization.


## About

This TypeScript SDK client supports the [Fetch API](https://fetch.spec.whatwg.org/)
and is automatically generated by the
[OpenAPI Generator](https://openapi-generator.tech) project:

- API version: `1.0.0`
- Package version: `1.0.0`
- Generator version: `7.21.0-SNAPSHOT`
- Build package: `org.openapitools.codegen.languages.TypeScriptFetchClientCodegen`

The generated npm module supports the following:

- Environments
  * Node.js
  * Webpack
  * Browserify
- Language levels
  * ES5 - you must have a Promises/A+ library installed
  * ES6
- Module systems
  * CommonJS
  * ES6 module system


## Development

### Building

To build the TypeScript source code, you need to have Node.js and npm installed.
After cloning the repository, navigate to the project directory and run:

```bash
npm install
npm run build
```

### Publishing

Once you've built the package, you can publish it to npm:

```bash
npm publish
```

## License

[]()
