# Streamer Ranker
## Svelte and Django Project

StreamerRanker is a platform where users can rate their favorite streamers, and discover new streamers to watch and enjoy.

This project is a simple example of how to use Svelte and Django together. It is a GPL open source project, being built by the ToluAfo community at https://twitch.tv/toluafo.

## Getting Started

To get started with this project, you will need to have:

* Node.js
* Python 3

Once you have all of the required dependencies, you can follow these steps to spin up the project:

1. Clone the repository from GitHub.
2. Traverse to the `twitch-rate` directory by running `cd twitch-rate`
3. Install the Svelte project dependencies by running `npm install`.
4. Traverse to the `streamer_ranker_api` directory by running `cd streamer_ranker_api`
5. This project uses pipenv to manage packages, install here: https://pipenv.pypa.io/en/latest/installation/.
6. Run `pipenv install` from the same directory as the pipfile
7. Run `python manage.py migrate` to create the database tables.
8. Run `manage.py runserver` to start the development server.
9. In another terminal run `npm run dev` to run the frontend

The frontend and backend will be available at http://localhost:8000 and http://localhost:5173 respectively by default.

## Contributing

To contribute to this project, you can fork the repository and create a pull request. Please make sure that your code is well-formatted and that you have followed the coding standards.

Consider joining the [ToluAfo Discord](https://discord.gg/y4qqfKZhTq) If you wish to contribute. 

## License

This project is licensed under the GPL v3 license.
  
