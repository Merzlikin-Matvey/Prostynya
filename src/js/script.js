const express = require("express");
const path = require("path");
const { newTask } = require("./gameHandler");

const app = express();
const PORT = 3000;

const projectDirectory = path.join(__dirname, "..", "..");

app.use(express.urlencoded({ extended: true }));

app.use(express.static(path.join(__dirname, "..", "/css")));

app.get("/", (req, res) => {
  res.sendFile(projectDirectory + "/src/html/mainPage.html");
});

app.get("/createFilePage", (req, res) => {
  res.sendFile(projectDirectory + "/src/html/createFilePage.html");
});

app.get("/gameModePage", (req, res) => {
  res.sendFile(projectDirectory + "/src/html/gameModePage.html");
});

app.get("/gamePage", (req, res) => {
  res.sendFile(projectDirectory + "/src/html/gamePage.html");
});

app.get("/resultPage", (req, res) => {
  res.sendFile(projectDirectory + "/src/html/resultPage.html");
});

app.post("/create_file", require("./createFileHandler").generateFile);

app.post("/start_game", require("./gameHandler").redirect);

app.post("/new_task", (req, res) => {
  res.send(newTask(Number(req.body.size), "Addition"));
});

app.get("/result", (req, res) => {
  res.redirect(
    "/resultPage" + "?num=" + req.body.num + "&result=" + req.body.result
  );
});

app.post("/download", (req, res) => {
    res.setHeader('Content-Disposition', `attachment; filename="00317SEP230742_solution.pdf"`);
    res.sendFile("C:\\Users\\User\\Desktop\\newProstynya\\Prostynya\\latex\\00317SEP230742_solution.pdf");
})

app.listen(PORT, () => {
  console.log(`Сервер запущен на порту ${PORT}`);
});
