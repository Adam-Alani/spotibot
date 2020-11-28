const Discord = require("discord.js");
const { prefix, token } = require('./config.json');
const client = new Discord.Client();
client.login(token);

var spotifyApi = new SpotifyWebApi({
    clientId: 'e31b1a401de04f70ae0e8b00c14425ca',
    clientSecret: '9af22fa28aec4e018c8829fdf8aa658a',
    redirectUri: 'http://www.example.com/callback'
    }
);

var scopes = ['user-read-private', 'playlist-read-private' , 'playlist-read-collaborative']
var authorizeURL = spotifyApi.createAuthorizeURL(scopes);


// ------------------ Commands ----------------------

client.on('message' , message => {
    if (!message.content.startsWith(prefix) || message.author.bot) return;

    const args = message.content.slice(prefix.length).trim().split(/ +/);
    const command = args.shift().toLowerCase();
    if (command === 'joinsp') {
        if (!args.length) {
            return message.channel.send(`Please enter playlist name, ${message.author}!`);
        }
    
        message.channel.send(`Command name: ${command}\nArguments: ${args}`);
        let playlist_name = args.join(" ");
        console.log(playlist_name)
    }

});

// ---------------------------------------------- // 

// Fetch playlist

spotifyApi.searchPlaylists('workout')
  .then(function(data) {
    console.log('Found playlists are', data.body);
  }, function(err) {
    console.log('Something went wrong!', err);
  });

