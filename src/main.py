import textnode

def main():
    new_textnode = textnode.TextNode("This is some anchor text", textnode.TextType.link_text, "www.example.com")

    print(new_textnode)


main()
