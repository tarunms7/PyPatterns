# Document Interface
class Document:
    def read(self):
        pass

# Concrete Classes
class PDFDocument(Document):
    def read(self):
        return "Reading a PDF document"

class WordDocument(Document):
    def read(self):
        return "Reading a Word document"

class TextDocument(Document):
    def read(self):
        return "Reading a Text document"

# Document Factory
class DocumentFactory:
    @staticmethod
    def create_document(file_extension):
        if file_extension == "pdf":
            return PDFDocument()
        elif file_extension == "docx":
            return WordDocument()
        elif file_extension == "txt":
            return TextDocument()
        else:
            raise ValueError(f"Unknown document type: {file_extension}")

# Example usage
if __name__ == "__main__":
    file_extension = input("Enter document type (pdf, docx, txt): ").lower()
    document = DocumentFactory.create_document(file_extension)
    print(document.read())
