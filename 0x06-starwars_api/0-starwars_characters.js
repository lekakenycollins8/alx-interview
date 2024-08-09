#!/usr/bin/node

const request = require('request');
// Get movie ID from command-line argument
const movie_id = process.argv[2];
// url of specific movie
const url = `https://swapi-api.alx-tools.com/api/films/${movie_id}/`;

const fetchCharacterNames = async () => {
    request(url, (error, response, body) => {
        if (error) {
            console.log(error);
        } else {
            // Parse movie data
            const movie = JSON.parse(body);
            const characters = movie.characters;

            // Create an array of promises to handle requests
            const promises = characters.map((character) => {
                return new Promise((resolve, reject) => {
                    request(character, (error, response, body) => {
                        if (error) {
                            reject(error);
                        } else {
                            const characterData = JSON.parse(body);
                            resolve(characterData.name);
                        }
                    });
                });
            });
            // Resolve all promises and print character names
            Promise.all(promises).then((names) => {
                names.forEach((name) => console.log(name));
            }).catch((error) => console.log(error));
        }
    });
};

// Call fetchCharacterNames function
fetchCharacterNames();