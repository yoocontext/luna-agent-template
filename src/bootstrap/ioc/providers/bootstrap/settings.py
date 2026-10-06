# pyright: reportUnknownVariableType=false

from dishka import Provider, Scope, provide

from bootstrap.settings import (
    PgSettings,
    RedisSettings,
    RmqSettings,
    S3Settings,
    Settings,
)


class SettingsProvider(Provider):
    @provide(scope=Scope.APP)
    def settings(self) -> Settings:
        return Settings()

    @provide(scope=Scope.APP)
    def pg_settings(self, settings: Settings) -> PgSettings:
        return settings.pg

    @provide(scope=Scope.APP)
    def redis_settings(self, settings: Settings) -> RedisSettings:
        return settings.redis

    @provide(scope=Scope.APP)
    def rmq_settings(self, settings: Settings) -> RmqSettings:
        return settings.rmq

    @provide(scope=Scope.APP)
    def s3_settings(self, settings: Settings) -> S3Settings:
        return settings.s3
