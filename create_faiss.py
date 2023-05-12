from sentence_transformers import SentenceTransformer
import torch 
from embeddings import create_faiss_files, read_all_files_in_folder

device = 'cuda' if torch.cuda.is_available() else 'cpu'
retriever = SentenceTransformer("flax-sentence-embeddings/all_datasets_v3_mpnet-base", device=device)

folder_path = "taxinfo"
UK_TAX_DOCUMENT_TEXT = read_all_files_in_folder(folder_path)

EMBEDDINGS_FILE = "embeddings.pt"
QUESTIONS_FILE = "questions.txt"

create_faiss_files(retriever, UK_TAX_DOCUMENT_TEXT, EMBEDDINGS_FILE, QUESTIONS_FILE)
