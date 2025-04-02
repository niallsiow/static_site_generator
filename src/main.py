import textnode

def main():
    new_textnode = textnode.TextNode("This is some anchor text", textnode.TextType.LINK, "www.example.com")

    print(new_textnode)


if __name__ == "__main__":
    main()
