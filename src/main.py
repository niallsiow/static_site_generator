import textnode

def main():
    new_textnode = textnode.TextNode("This is some anchor text", textnode.TextType.LINK, "www.example.com")

    print(new_textnode)


main()
