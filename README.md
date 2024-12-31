# RAG Development Environment

## Steps to use Ollama

1.  **Set Up Ollama Requirements:**

    - Follow the instructions at [Ollama Download](https://ollama.com/download) to download and install Ollama for your environment.
    - After installing Ollama, setup the required models using the following commands:

      ```sh
      ollama run llama3.2
      ollama run nomic-embed-text
      ```

    - Ensure you have the correct configuration settings for Ollama in your environment.

2.  **Check Ollama Status (Host):**

    - Use the following `curl` command to check if Ollama is up and running:

      ```sh
      curl http://localhost:11434
      ```

    - You should see the below output:

      ```sh
      Ollama is running
      ```

## Steps to use Dev Containers

1. **Install Docker Desktop**:
   - Ensure Docker Desktop is installed on your machine. You can download and install it from [here](https://www.docker.com/products/docker-desktop).
   - Enable Host Networking under `Settings -> Resources -> Network` in Docker Desktop.

2. **Install Visual Studio Code**:
   - Ensure Visual Studio Code is installed on your machine. You can download and install it from [here](https://code.visualstudio.com/).

3. **Install Dev Containers Extension**:
   - Open Visual Studio Code.
   - Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or by pressing `Ctrl+Shift+X`.
   - Search for `Dev Containers` and install the extension provided by Microsoft.

4. **Open the Project in a Dev Container**:
   - Open the project folder in Visual Studio Code.
   - Press `F1` or `Ctrl+Shift+P` to open the Command Palette.
   - Type `Dev Containers: Reopen in Container` and select it if you are building it for the first time.
   - Type `Dev Containers: Rebuild and Reopen in Container` and select it if you have already used it before.
   - Visual Studio Code will build the Docker image defined in the `.devcontainer/Dockerfile` and open the project inside the container.

5. **Start Developing**:
   - Once the container is up and running, you can start developing your project.
   - The container will have all the necessary dependencies and tools installed as defined in the `.devcontainer/Dockerfile`.

6. **Accessing the Terminal**:
   - You can access the terminal inside the container by opening the Terminal view in Visual Studio Code (`` Ctrl+` ``).

7.  **Check Ollama Status (Dev Container):**

    - Use the following `curl` command to check if Ollama is up and running:

      ```sh
      curl http://localhost:11434
      ```

    - You should see the below output:

      ```sh
      Ollama is running
      ```

8. **Stopping the Container**:
   - To stop the container, simply close Visual Studio Code or use the Docker Dashboard to stop the container manually.

9. **Rebuilding the Container**:
   - If you make changes to the `.devcontainer/Dockerfile` or `.devcontainer/devcontainer.json`, you may need to rebuild the container.
   - You can do this by pressing `F1` or `Ctrl+Shift+P` to open the Command Palette, typing `Dev Containers: Rebuild Container`, and selecting it.


## Steps to execute

1.  **Populate the Database (Optional):**

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

2.  **Query the Database:**

    - To query the database, run the `query_app.py` script with the query text as an argument.

      ```sh
      python query_app.py "Your query text here"
      ```
