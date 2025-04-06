import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        
        for i in range(len(sections)):
            if sections[i] == "":
                continue

            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))

        new_nodes.extend(split_nodes)

        return new_nodes


def extract_markdown_images(text):
    alt_texts = re.findall(r"!\[(.*?)\]", text)
    image_urls = re.findall(r"\((.*?)\)", text)
    return list(zip(alt_texts, image_urls))


def extract_markdown_links(text):
    anchor_texts = re.findall(r"\[(.*?)\]", text) 
    link_urls = re.findall(r"\((.*?)\)", text)
    return list(zip(anchor_texts, link_urls)) 