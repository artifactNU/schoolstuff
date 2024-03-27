# from GenericDocument import GenericDocument
# from PartType import PartType


# class HTMLDocument(GenericDocument):
#     def __init__(self):
#         self.parts = []

#     def add_part(self, part_type, content):
#         if part_type == PartType.HEADING1:
#             self.parts.append(f"<h1>{content}</h1>")
#         elif part_type == PartType.HEADING2:
#             self.parts.append(f"<h2>{content}</h2>")
#         elif part_type == PartType.HEADING3:
#             self.parts.append(f"<h3>{content}</h3>")
#         elif part_type == PartType.PARAGRAPH:
#             self.parts.append(f"<p>{content}</p>")
#         elif part_type == PartType.CODEBLOCK:
#             self.parts.append(f"<pre><code>{content}</code></pre>")

#     def render(self):
#         return "\n".join(self.parts)

#     @classmethod
#     def escape_html(cls, content):
#         return (
#             content.replace("&", "&amp;")
#             .replace("<", "&lt;")
#             .replace(">", "&gt;")
#             .replace('"', "&quot;")
#             .replace("'", "&#39;")
#         )

# -------------------------------------------

# from GenericDocument import GenericDocument


# class HTMLDocument(GenericDocument):
#     def __init__(self):
#         super().__init__()

#     def add_heading1(self, text):
#         self.list_document_parts.append(f"<h1>{self.escape_html(text)}</h1>")
#         return self

#     def add_heading2(self, text):
#         self.list_document_parts.append(f"<h2>{self.escape_html(text)}</h2>")
#         return self

#     def add_heading3(self, text):
#         self.list_document_parts.append(f"<h3>{self.escape_html(text)}</h3>")
#         return self

#     def add_paragraph(self, text):
#         self.list_document_parts.append(f"<p>{self.escape_html(text)}</p>")
#         return self

#     def add_codeblock(self, text):
#         self.list_document_parts.append(
#             f"<pre><code>{self.escape_html(text)}</code></pre>"
#         )
#         return self

#     # Implement the other methods...

#     @staticmethod
#     def escape_html(text):
#         return (
#             text.replace("&", "&amp;")
#             .replace("<", "&lt;")
#             .replace(">", "&gt;")
#             .replace('"', "&quot;")
#             .replace("'", "&#39;")
#         )

# --------------------------------------------

# from GenericDocument import GenericDocument


# class HTMLDocument(GenericDocument):
#     @classmethod
#     def escape_html(cls, text):
#         return (
#             text.replace("&", "&amp;")
#             .replace("<", "&lt;")
#             .replace(">", "&gt;")
#             .replace('"', "&quot;")
#             .replace("'", "&#39;")
#         )

#     def render_heading1(self, text):
#         return f"<h1>{self.escape_html(text)}</h1>"

#     def render_heading2(self, text):
#         return f"<h2>{self.escape_html(text)}</h2>"

#     def render_heading3(self, text):
#         return f"<h3>{self.escape_html(text)}</h3>"

#     def render_paragraph(self, text):
#         text = text.replace("\n", "<br>")
#         return f"<p>{self.escape_html(text)}</p>"

#     def render_codeblock(self, text):
#         return f"<pre><code>{self.escape_html(text)}</code></pre>"

# ------------------------------------------
from GenericDocument import GenericDocument


class HTMLDocument(GenericDocument):
    @classmethod
    def escape_html(cls, text):
        return (
            text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#39;")
        )

    def render_heading1(self, text):
        text = self.escape_html(text).replace("\n", "<br>")
        return f"<h1>{text}</h1>"

    def render_heading2(self, text):
        text = self.escape_html(text).replace("\n", "<br>")
        return f"<h2>{text}</h2>"

    def render_heading3(self, text):
        text = self.escape_html(text).replace("\n", "<br>")
        return f"<h3>{text}</h3>"

    def render_paragraph(self, text):
        text = self.escape_html(text).replace("\n", "<br>")
        return f"<p>{text}</p>"

    def render_codeblock(self, text):
        return f"<pre><code>{self.escape_html(text)}</code></pre>"

    # ------------------
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
