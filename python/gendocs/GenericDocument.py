# from abc import ABC, abstractmethod


# class GenericDocument(ABC):
#     def __init__(self):
#         super().__init__()

#     @abstractmethod
#     def add_part(self, part_type, content):
#         pass

#     @abstractmethod
#     def render(self):
#         pass

# -----------------------

# from abc import ABC, abstractmethod


# class GenericDocument(ABC):
#     def __init__(self):
#         self.list_document_parts = []

#     @abstractmethod
#     def add_heading1(self, text):
#         pass

#     @abstractmethod
#     def add_heading2(self, text):
#         pass

#     @abstractmethod
#     def add_heading3(self, text):
#         pass

#     @abstractmethod
#     def add_paragraph(self, text):
#         pass

#     @abstractmethod
#     def add_codeblock(self, text):
#         pass

#     @abstractmethod
#     def merge_indices(self, dst_index, *src_indices, sep):
#         pass

#     @abstractmethod
#     def merge_consecutive(self, partType):
#         pass

#     @abstractmethod
#     def render(self):
#         pass

#     @abstractmethod
#     def render_paragraph(self, text):
#         pass

#     @abstractmethod
#     def __getitem__(self, index):
#         pass

#     @abstractmethod
#     def __len__(self):
#         pass

# --------------------
from abc import ABC, abstractmethod
from PartType import PartType


class GenericDocument(ABC):
    def __init__(self):
        self._document_parts = []

    def add_heading1(self, text):
        self._document_parts.append((PartType.HEADING1, text))
        return self

    def add_heading2(self, text):
        self._document_parts.append((PartType.HEADING2, text))
        return self

    def add_heading3(self, text):
        self._document_parts.append((PartType.HEADING3, text))
        return self

    def add_paragraph(self, text):
        self._document_parts.append((PartType.PARAGRAPH, text))
        return self

    def add_codeblock(self, text):
        self._document_parts.append((PartType.CODEBLOCK, text))
        return self

    def merge_indices(self, dst_index, *src_indices, sep="\n"):
        if dst_index in src_indices:
            raise ValueError("Destination index cannot be in source indices.")
        src_texts = [self._document_parts[i][1] for i in sorted(set(src_indices))]
        self._document_parts[dst_index] = (
            self._document_parts[dst_index][0],
            sep.join([self._document_parts[dst_index][1]] + src_texts),
        )
        for i in sorted(set(src_indices), reverse=True):
            del self._document_parts[i]
        return self

    def merge_consecutive(self, partType, sep="\n"):
        i = 0
        while i < len(self._document_parts) - 1:
            current_type, current_text = self._document_parts[i]
            next_type, next_text = self._document_parts[i + 1]
            if current_type == next_type == partType:
                self._document_parts[i] = (
                    current_type,
                    sep.join([current_text, next_text]),
                )
                del self._document_parts[i + 1]
            else:
                i += 1
        return self

    def __getitem__(self, index):
        return self._document_parts[index]

    def __len__(self):
        return len(self._document_parts)

    @abstractmethod
    def render_paragraph(self, text):
        pass

    def render_heading1(self, text):
        return self.render_paragraph(text)

    def render_heading2(self, text):
        return self.render_heading1(text)

    def render_heading3(self, text):
        return self.render_heading2(text)

    def render_codeblock(self, text):
        return self.render_paragraph(text)

    # def render_heading2(self, text):
    #     return self.render_paragraph(text)

    # def render_heading3(self, text):
    #     return self.render_paragraph(text)

    # def render(self):
    #     result = ""
    #     for part_type, text in self._document_parts:
    #         render_method_name = "render_" + part_type.name.lower()
    #         if hasattr(self, render_method_name):
    #             render_method = getattr(self, render_method_name)
    #             part_result = render_method(text)
    #         else:
    #             part_result = self.render_paragraph(text)
    #         result += part_result
    #     return result

    # def render(self):
    #     result = ""
    #     for part_type, text in self._document_parts:
    #         render_method_name = "render_" + part_type.name.lower()
    #         if hasattr(self, render_method_name):
    #             render_method = getattr(self, render_method_name)
    #             part_result = render_method(text)
    #         elif "heading" in part_type.name.lower():
    #             part_result = self.render_heading1(text)
    #         else:
    #             part_result = self.render_paragraph(text)
    #         result += part_result
    #     return result

    def render(self):
        result = ""
        for part_type, text in self._document_parts:
            render_method_name = "render_" + part_type.name.lower()
            if hasattr(self, render_method_name):
                render_method = getattr(self, render_method_name)
                part_result = render_method(text)
            elif "heading3" in part_type.name.lower():
                part_result = self.render_heading2(text)
            elif "heading" in part_type.name.lower():
                part_result = self.render_heading1(text)
            else:
                part_result = self.render_paragraph(text)
            result += part_result
        return result
