# from GenericDocument import GenericDocument
# from PartType import PartType


# class MarkdownDocument(GenericDocument):
#     def __init__(self):
#         self.parts = []

#     def add_part(self, part_type, content):
#         if part_type == PartType.HEADING1:
#             self.parts.append(f"# {content}")
#         elif part_type == PartType.HEADING2:
#             self.parts.append(f"## {content}")
#         elif part_type == PartType.HEADING3:
#             self.parts.append(f"### {content}")
#         elif part_type == PartType.PARAGRAPH:
#             self.parts.append(f"{content}\n\n")
#         elif part_type == PartType.CODEBLOCK:
#             self.parts.append(f"```\n{content}\n```")

#     def render(self):
#         return "\n".join(self.parts)

# --------------------------------------

# from GenericDocument import GenericDocument


# class MarkdownDocument(GenericDocument):
#     def __init__(self):
#         super().__init__()

#     def add_heading1(self, text):
#         self.list_document_parts.append(f"# {text}")
#         return self

#     def add_heading2(self, text):
#         self.list_document_parts.append(f"## {text}")
#         return self

#     def add_heading3(self, text):
#         self.list_document_parts.append(f"### {text}")
#         return self

#     def add_paragraph(self, text):
#         self.list_document_parts.append(f"{text}\n\n")
#         return self

#     def add_codeblock(self, text):
#         self.list_document_parts.append(f"```\n{text}\n```")
#         return self

#     # Implement the other methods...

#     def render(self):
#         return "\n".join(self.list_document_parts)

# ----------------------------

# from GenericDocument import GenericDocument


# class MarkdownDocument(GenericDocument):
#     def render_heading1(self, text):
#         return f"# {text}\n\n"

#     def render_heading2(self, text):
#         return f"## {text}\n\n"

#     def render_heading3(self, text):
#         return f"### {text}\n\n"

#     def render_paragraph(self, text):
#         return f"{text}\n\n"

#     def render_codeblock(self, text):
#         return f"```\n{text}\n```\n\n"

# ------------------------------
from GenericDocument import GenericDocument


class MarkdownDocument(GenericDocument):
    def render_heading1(self, text):
        text = text.replace("`", "\\`").replace("\n", " ")
        return f"# {text}\n\n"

    def render_heading2(self, text):
        text = text.replace("`", "\\`").replace("\n", " ")
        return f"## {text}\n\n"

    def render_heading3(self, text):
        text = text.replace("`", "\\`").replace("\n", " ")
        return f"### {text}\n\n"

    def render_paragraph(self, text):
        text = text.replace("`", "\\`")
        return f"{text}\n\n"

    def render_codeblock(self, text):
        text = text.replace("`", "\\`")
        return f"```\n{text}\n```\n\n"

    # -----------------
    # def render(self):
    #     result = ""
    #     for part_type, text in self._document_parts:
    #         if part_type == PartType.HEADING1:
    #             result += self.render_heading1(text)
    #         elif part_type == PartType.HEADING2:
    #             result += self.render_heading2(text)
    #         elif part_type == PartType.HEADING3:
    #             result += self.render_heading3(text)
    #         elif part_type == PartType.PARAGRAPH:
    #             result += self.render_paragraph(text)
    #         elif part_type == PartType.CODEBLOCK:
    #             result += self.render_codeblock(text)
    #         else:
    #             raise Exception(f"Unsupported part type: {part_type}")
    #     return result
