# pyright: reportUnknownVariableType=false

from dishka import Provider, Scope, provide
from redis.asyncio import Redis

from bootstrap.settings import RedisSettings


class RedisProvider(Provider):
    def __init__(
        self,
        redis_client: Redis | None = None,
    ) -> None:
        super().__init__()
        self.redis_client: Redis | None = redis_client

    @provide(scope=Scope.APP)
    def redis(
        self,
        settings: RedisSettings,
    ) -> Redis:
        if self.redis_client:
            return self.redis_client

        else:
            return Redis(
                host=settings.host,
                port=settings.port,
                db=settings.db,
                password=settings.password,
            )
