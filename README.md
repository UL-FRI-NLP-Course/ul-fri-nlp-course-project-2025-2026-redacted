# Redacted
A repository for the project for Natural Language Processing .

## reproduction

You can run the chatbot for yourself on any machine that has singularity installed, such as the HPC sluster.

To help with this, there are a few provided scripts.

`container_setup.sh` sets up the singularity container required to run the indexing and the chatbot from the `containder.def` template.

Then once the container is created, you must first index your dat, some data is already included in the repository.

To index the data run `build_index.sh` and wait for it to complete.

Once the data is indexed, you can run `chatbot.sh` to start the chatbot.

enjoy.
