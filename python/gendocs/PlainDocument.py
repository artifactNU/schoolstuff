# from GenericDocument import GenericDocument
# from PartType import PartType


# class PlainDocument(GenericDocument):
#     def __init__(self):
#         self.parts = []

#     def add_part(self, part_type, content):
#         if part_type == PartType.HEADING1:
#             self.parts.append(f"{content}\n\n")
#         elif part_type == PartType.HEADING2:
#             self.parts.append(f"{content}\n\n")
#         elif part_type == PartType.HEADING3:
#             self.parts.append(f"{content}\n\n")
#         elif part_type == PartType.PARAGRAPH:
#             self.parts.append(f"{content}\n\n")
#         elif part_type == PartType.CODEBLOCK:
#             self.parts.append(f"{content}\n\n")

#     def render(self):
#         return "".join(self.parts)

# -------------------------------

# from GenericDocument import GenericDocument


# class PlainDocument(GenericDocument):
#     def __init__(self):
#         super().__init__()

#     def add_heading1(self, text):
#         self.list_document_parts.append(f"{text}\n")
#         return self

#     def add_heading2(self, text):
#         self.list_document_parts.append(f"{text}\n")
#         return self

#     def add_heading3(self, text):
#         self.list_document_parts.append(f"{text}\n")
#         return self

#     def add_paragraph(self, text):
#         self.list_document_parts.append(f"{text}\n\n")
#         return self

#     def add_codeblock(self, text):
#         self.list_document_parts.append(f"```\n{text}\n```\n")
#         return self

#     # Implement the other methods...

#     def render(self):
#         return "".join(self.list_document_parts)

# --------------------------------------

from GenericDocument import GenericDocument


class PlainDocument(GenericDocument):
    def render_paragraph(self, text):
        # For PlainDocument, we just return the text followed by two newline characters.
        # This ensures an empty line between each document part, making it plain text.
        return f"{text}\n\n"
