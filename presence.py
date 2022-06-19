from time import sleep
from pypresence import Presence


def main():

    RPC = Presence(888278703975579698)
    RPC.connect()

    RPC.update(
        large_text="鯊妹(サメちゃん)",
        state="鯊妹(サメちゃん)",
        details="多功能discord bot",
        large_image="shark",
        start=999999999999,
        buttons=[
            {
                "label": "邀請連結",
                "url": "https://discordservers.tw/bots/888278703975579698",
            },
            {
                "label": "支援群",
                "url": "https://discordservers.tw/servers/930958107042013205",
            },
        ],
    )
    while True:
        sleep(15)


if __name__ == "__main__":
    main()
