class AppError(Exception):
    def __init__(self, detail: str, status_code: int = 400):
        super().__init__(detail)
        self.detail: str = detail
        self.status_code: int = status_code


class BadRequestError(AppError):
    def __init__(self, detail: str = "Bad Request"):
        super().__init__(detail, status_code=400)


class UnauthorizedError(AppError):
    def __init__(self, detail: str = "Unauthorized"):
        super().__init__(detail, status_code=401)


class ForbiddenError(AppError):
    def __init__(self, detail: str = "Forbidden"):
        super().__init__(detail, status_code=403)


class NotFoundError(AppError):
    def __init__(self, detail: str = "Not Found"):
        super().__init__(detail, status_code=404)


class ConflictError(AppError):
    def __init__(self, detail: str = "Conflict"):
        super().__init__(detail, status_code=409)


class UnprocessableEntityError(AppError):
    def __init__(self, detail: str = "Unprocessable Entity"):
        super().__init__(detail, status_code=422)


