from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    REF_ID: str = '0000369k'

Hey, if you're a Hamster, DOGS, Blum or Catizen user... you have something very special to claim in the Tomarket app now.

The Tomarket airdrop is coming! 🪂

Claim with this link.'
    
    FAKE_USERAGENT: bool = True
    AUTO_PLAY_GAME: bool = True
    AUTO_TASK: bool = True
    AUTO_DAILY_REWARD: bool = True
    AUTO_CLAIM_STARS: bool = True
    AUTO_CLAIM_COMBO: bool = True

    USE_RANDOM_DELAY_IN_RUN: bool = True
    RANDOM_DELAY_IN_RUN: list[int] = [0, 15]

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()

