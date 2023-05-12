import torch
import faiss
import os

def split_text_to_paragraphs(text, delimiter="\n"):
    return text.strip().split(delimiter)

def create_faiss_files(retriever, document_text, embeddings_file, questions_file, delimiter="\n"):
    paragraphs = split_text_to_paragraphs(document_text, delimiter)
    embeddings = retriever.encode(paragraphs, batch_size=1).astype("float32")
    torch.save(embeddings, embeddings_file)
    with open(questions_file, "w") as f:
        f.write("\n".join(paragraphs))

def load_faiss_index(embeddings_file, questions_file):
    embeddings = torch.load(embeddings_file)
    with open(questions_file, "r") as f:
        questions = [line.strip() for line in f.readlines()]

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index, questions

def query_faiss(retriever, faiss_index, questions, query, top_k):
    xq = retriever.encode([query], batch_size=1).astype("float32")
    distances, indices = faiss_index.search(xq, top_k)
    matches = [{"metadata": {"paragraph": questions[i]}, "score": 1 - d} for i, d in zip(indices[0], distances[0])]
    return matches

def read_all_files_in_folder(folder_path, encoding="utf-8"):
    all_files_content = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding=encoding) as f:
                file_content = f.read()
                all_files_content.append(file_content)
    return "\n".join(all_files_content)
