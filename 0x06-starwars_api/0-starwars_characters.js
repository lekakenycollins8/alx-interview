const request = require('request');

const movie_id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movie_id}/`;

request(url, (error, response, body) => {
    if (error) {
        console.log(error);
    } else {
        const movie = JSON.parse(body);
        const characters = movie.characters;
        characters.forEach((character) => {
            request(character, (error, response, body) => {
                if (error) {
                    console.log(error);
                } else {
                    const character = JSON.parse(body);
                    console.log(character.name);
                }
            });
        });
    }
});