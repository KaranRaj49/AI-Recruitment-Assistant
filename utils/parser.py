from langchain_core.output_parsers import StrOutputParser

def get_parser():
    """Returns a simple string output parser."""
    return StrOutputParser()