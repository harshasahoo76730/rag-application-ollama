import argparse

from get_embedding import get_embedding_function
from langchain.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM


MODEL = "llama3.2"
CHROMA_PATH = "chroma"
PROMPT_TEMPLATE = """
You are a helpful assistant.
You are asked a question and you provide an answer in a friendly and informative manner.
Answer the question based on the above information: {question}
"""
PROMPT_TEMPLATE_WITH_CONTEXT = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""


def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="Query Text")
    parser.add_argument("--model", type=str, default=MODEL, help="Model Name")
    parser.add_argument("--no_context", action="store_true",
                        help="Disable Context")
    args = parser.parse_args()
    query_text = args.query_text
    model_name = args.model
    no_context = args.no_context
    query_rag(query_text, model_name, no_context)


def query_rag(query_text: str, model_name: str, no_context: bool):
    if not no_context:
        # Prepare DB
        embedding_function = get_embedding_function()
        db = Chroma(persist_directory=CHROMA_PATH,
                    embedding_function=embedding_function)

        # Search DB
        results = db.similarity_search_with_score(query_text, k=5)

        # Context Text
        context_text = "\n\n---\n\n".join(
            [doc.page_content for doc, _score in results])
        sources = [doc.metadata.get("id", None) for doc, _score in results]

        prompt_template_with_context = ChatPromptTemplate.from_template(
            PROMPT_TEMPLATE_WITH_CONTEXT)
        prompt = prompt_template_with_context.format(
            context=context_text, question=query_text)
    else:
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(question=query_text)

    model = OllamaLLM(model=model_name)
    response_text = model.invoke(prompt)

    if not no_context:
        formatted_response = f"✅ Model: {model_name}\n✅ Response: {response_text}\n✅ Sources: {sources}"
    else:
        formatted_response = f"✅ Model: {model_name}\n✅ Response: {response_text}"
    print(formatted_response)
    return response_text


if __name__ == "__main__":
    main()
