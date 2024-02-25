# main.py

from query_gpt import query_gpt_with_ttl_ontology

def main():
    question = input("Enter your question: ")
    answer = query_gpt_with_ttl_ontology(question)
    print("Answer:", answer)

if __name__ == "__main__":
    main()
