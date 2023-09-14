const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;

const { createFiles } = require('./generate_tasks');

const projectDirectory = path.join(__dirname, '..', '..');

app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.sendFile(projectDirectory + '/src/html/main.html');
});

app.get('/createFilePage', (req, res) => {
    res.sendFile(projectDirectory + '/src/html/create_file.html')
});

app.post('/create_file', (req, res) => {
    const num = Number(req.body.num)
    const size = Number(req.body.size)
    const title = String(req.body.title)
    const fileName = String(req.body.fileName)

    createFiles(num, 
                size, 
                "Addition", 
                title,
                fileName)

    const filePath = path.join(projectDirectory, 'latex', fileName + ".pdf");

    res.setHeader('Content-Disposition', `attachment; filename="${fileName}.pdf"`);
    res.sendFile(filePath);

    res.sendFile(projectDirectory + "\\latex\\" + fileName + ".pdf")
});

app.listen(PORT, () => {
    console.log(`Сервер запущен на порту ${PORT}`);
});
