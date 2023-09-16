const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;

const { createFiles } = require('./tasks');

const projectDirectory = path.join(__dirname, '..', '..');

app.use(express.urlencoded({ extended: true }));

app.use(express.static(path.join(__dirname, '..', '/css')))

app.get('/', (req, res) => {
    res.sendFile(projectDirectory + '/src/html/mainPage.html');
});

app.get('/createFilePage', (req, res) => {
    res.sendFile(projectDirectory + '/src/html/createFilePage.html')
});

app.get('/gameModePage', (req, res) => {
    res.sendFile(projectDirectory + '/src/html/gameModePage.html')
});

app.post('/create_file', require('./createFileHandler'));

app.listen(PORT, () => {
    console.log(`Сервер запущен на порту ${PORT}`);
});
