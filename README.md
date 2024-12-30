# rag-development-environment

## Steps to Use

1.  **Set Up Ollama Requirements:**

    - Follow the instructions at [Ollama Download](https://ollama.com/download) to download and install Ollama for your environment.
    - After installing Ollama, setup the required models using the following commands:

      ```sh
      ollama run llama3.2
      ollama run nomic-embed-text
      ```

    - Ensure you have the correct configuration settings for Ollama in your environment.

2.  **Check Ollama Status:**

    - Use the following `curl` command to check if Ollama is up and running:

      ```sh
      curl http://localhost:11434
      ```

    - You should see the below output:

      ```sh
      Ollama is running
      ```

3.  **Prepare the Environment:**

    - Ensure you have all the necessary dependencies installed. You can typically do this by running:

      ```sh
      pip install -r requirements.txt
      ```

4.  **Populate the Database:**

    - To add your own PDF files, place them in the `data` directory.
    - To remove PDF files, simply delete them from the `data` directory.
    - After adding or removing files, to populate the database with documents, run the `populate_database.py` script. This script will load documents from the `data` directory, split them into chunks, and add them to the Chroma database.

      ```sh
      python populate_database.py
      ```

    - If you want to reset the database before populating it, use the `--reset` flag:

      ```sh
      python populate_database.py --reset
      ```

5.  **Query the Database:**

    - To query the database, run the `query_app.py` script with the query text as an argument.

      ```sh
      python query_app.py "Your query text here"
      ```
