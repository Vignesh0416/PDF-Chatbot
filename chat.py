from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI,OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()
import os
import tempfile
import streamlit as st
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        temp_path = tmp_file.name

    loader = PyPDFLoader(temp_path)
    docs = loader.load()
    llm=ChatOpenAI(
        model='gpt-4o-mini',
        base_url='https://openrouter.ai/api/v1',
        api_key=os.getenv('OPENROUTER_API_KEY'),
        max_tokens=2000
    )
    prompt=ChatPromptTemplate.from_template(
    """
    You are an AI assistant
    Give answer based on the user question
    context
    {context}
    question
    {question}
    """
    )
    chain=prompt|llm|StrOutputParser()
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks=splitter.split_documents(docs)
    embedding=OpenAIEmbeddings(
        model='text-embedding-3-small',
        base_url='https://openrouter.ai/api/v1',
        api_key=os.getenv('OPENROUTER_API_KEY')
    )
    db=FAISS.from_documents(
        chunks,
        embedding
    )
    retreiver=db.as_retriever()
    st.title('PDF Chatbot')
    question=st.text_input('Enter Your Question')
    if st.button('Generate'):
        result=retreiver.invoke(question)
        context='\n\n'.join(
            i.page_content
            for i in result
        )
        answer=chain.invoke({
            "context":context,
            "question":question
        })
        st.write(answer)