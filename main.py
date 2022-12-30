from chat_downloader import ChatDownloader


def chat_listener(url: str):
    chat = ChatDownloader().get_chat(url)
    for message in chat:
        chat.print_formatted(message)


def main():
    url = input("URL: ")
    chat_listener(url)


if __name__ == "__main__":
    main()
